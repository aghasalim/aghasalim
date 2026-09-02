# Recompute derived fields of reports/demo_status.json in Ruby.
#
# Reads the script constants from scripts/ping_demos.py, loads the JSON report,
# and checks thin/woken/url/attempts against the raw measurements.
#
# Run: ruby verify/status.rb <repo root>

require "json"

root = ARGV[0] || "."

script = File.read(File.join(root, "scripts", "ping_demos.py"), encoding: "UTF-8")
report = JSON.parse(File.read(File.join(root, "reports", "demo_status.json"), encoding: "UTF-8"))

floor_val    = script[/\nCONTENT_FLOOR\s*=\s*(\d+)/, 1].to_i
attempts_val = script[/\nATTEMPTS\s*=\s*(\d+)/, 1].to_i
demos_block  = script[/\nDEMOS\s*=\s*\{(.*?)\n\}/m, 1]
demos = {}
demos_block.scan(/"([^"]+)"\s*:\s*"([^"]+)"/) { |n, u| demos[n] = u }

bad = 0
fail_msg = ->(m) { puts "  FAIL: #{m}"; bad += 1 }

seen = {}
report["demos"].each do |r|
  seen[r["demo"]] = true
  want_woken = r["ok"] == true && r["was_asleep"] == true
  fail_msg.("#{r["demo"]}: woken should be #{want_woken}") if r["woken"] != want_woken
  if r["ok"]
    want_thin = r["chars"] < floor_val
    fail_msg.("#{r["demo"]}: thin should be #{want_thin}") if r["thin"] != want_thin
    fail_msg.("#{r["demo"]}: ok row without positive seconds") unless r["seconds"].is_a?(Numeric) && r["seconds"] > 0
  end
  unless r["attempts"].is_a?(Integer) && r["attempts"] >= 1 && r["attempts"] <= attempts_val
    fail_msg.("#{r["demo"]}: attempts outside 1..#{attempts_val}")
  end
  if demos.key?(r["demo"]) && demos[r["demo"]] != r["url"]
    fail_msg.("#{r["demo"]}: url disagrees with script")
  end
end

demos.each_key do |d|
  fail_msg.("#{d}: in script but absent from report") unless seen[d]
end

if bad > 0
  puts "Ruby: #{bad} problem(s)"
  exit 1
end
puts "Ruby: #{report["demos"].size} demo(s), thin/woken/url recomputed, CONTENT_FLOOR=#{floor_val}, ATTEMPTS=#{attempts_val}"
