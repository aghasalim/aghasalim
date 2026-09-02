// Recompute derived fields of reports/demo_status.json in Node.
//
// Reads the script constants from scripts/ping_demos.py with its own parser,
// loads the report, and checks thin/woken/url/attempts against the raw fields.
//
// Run: node verify/status.js <repo root>

const fs = require("fs");
const path = require("path");

const root = process.argv[2] || ".";
const script = fs.readFileSync(path.join(root, "scripts", "ping_demos.py"), "utf8");
const report = JSON.parse(fs.readFileSync(path.join(root, "reports", "demo_status.json"), "utf8"));

let bad = 0;
const fail = (m) => { console.log("  FAIL: " + m); bad++; };

const floor_val = parseInt(script.match(/\nCONTENT_FLOOR\s*=\s*(\d+)/)[1], 10);
const attempts_val = parseInt(script.match(/\nATTEMPTS\s*=\s*(\d+)/)[1], 10);
const demos_block = script.match(/\nDEMOS\s*=\s*\{([\s\S]*?)\n\}/)[1];
const demos = {};
for (const m of demos_block.matchAll(/"([^"]+)"\s*:\s*"([^"]+)"/g)) {
  demos[m[1]] = m[2];
}

const seen = new Set();
for (const row of report.demos) {
  seen.add(row.demo);
  const want_woken = row.ok === true && row.was_asleep === true;
  if (row.woken !== want_woken)
    fail(row.demo + ": woken should be " + want_woken);
  if (row.ok) {
    const want_thin = row.chars < floor_val;
    if (row.thin !== want_thin)
      fail(row.demo + ": thin should be " + want_thin);
    if (typeof row.seconds !== "number" || row.seconds <= 0)
      fail(row.demo + ": ok row without positive seconds");
  }
  if (typeof row.attempts !== "number" || row.attempts < 1 || row.attempts > attempts_val)
    fail(row.demo + ": attempts outside 1.." + attempts_val);
  if (demos[row.demo] !== undefined && demos[row.demo] !== row.url)
    fail(row.demo + ": url disagrees with script");
}

for (const name of Object.keys(demos)) {
  if (!seen.has(name)) fail(name + ": in script but absent from report");
}

if (bad) {
  console.log("JS: " + bad + " problem(s)");
  process.exit(1);
}
console.log("JS: " + report.demos.length + " demo(s), thin/woken/url recomputed, CONTENT_FLOOR=" + floor_val + ", ATTEMPTS=" + attempts_val);
