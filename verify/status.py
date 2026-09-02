"""Recompute derived fields of reports/demo_status.json in Python.

Shares NO code with scripts/ping_demos.py -- reads the same constants and
DEMOS table from the script's source with its own regex parser, then checks
thin/woken/url/attempts against the raw measurements.

Run: python3 verify/status.py <repo root>
"""
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
script = (root / "scripts" / "ping_demos.py").read_text(encoding="utf-8")
report = json.loads((root / "reports" / "demo_status.json").read_text(encoding="utf-8"))

floor_val = int(re.search(r"\nCONTENT_FLOOR\s*=\s*(\d+)", script).group(1))
attempts_val = int(re.search(r"\nATTEMPTS\s*=\s*(\d+)", script).group(1))
demos_block = re.search(r"\nDEMOS\s*=\s*\{(.*?)\n\}", script, re.S).group(1)
demos = dict(re.findall(r'"([^"]+)"\s*:\s*"([^"]+)"', demos_block))

bad = 0

def fail(msg):
    global bad
    print(f"  FAIL: {msg}")
    bad += 1

seen = set()
for r in report["demos"]:
    seen.add(r["demo"])
    want_woken = r.get("ok") is True and r.get("was_asleep") is True
    if r.get("woken") != want_woken:
        fail(f"{r['demo']}: woken should be {want_woken}")
    if r.get("ok"):
        want_thin = r["chars"] < floor_val
        if r.get("thin") != want_thin:
            fail(f"{r['demo']}: thin should be {want_thin}")
        if not isinstance(r.get("seconds"), (int, float)) or r["seconds"] <= 0:
            fail(f"{r['demo']}: ok row without positive seconds")
    att = r.get("attempts")
    if not isinstance(att, int) or att < 1 or att > attempts_val:
        fail(f"{r['demo']}: attempts outside 1..{attempts_val}")
    if r["demo"] in demos and demos[r["demo"]] != r.get("url"):
        fail(f"{r['demo']}: url disagrees with script")

for d in demos:
    if d not in seen:
        fail(f"{d}: in script but absent from report")

if bad:
    print(f"Python: {bad} problem(s)")
    sys.exit(1)
print(f"Python: {len(report['demos'])} demo(s), thin/woken/url recomputed, "
      f"CONTENT_FLOOR={floor_val}, ATTEMPTS={attempts_val}")
