"""Keep the Streamlit demos awake, and report the ones that were asleep.

Why a headless browser rather than curl: Streamlit Community Cloud serves the
SAME shell whether an app is running or asleep. A sleeping app returns HTTP 303
and a normal-looking page; the "Zzzz / Yes, get this app back up!" screen is
rendered client-side by JavaScript. I verified that directly -- ieee-fraud-ml
was fast asleep while curl reported exactly the same 303 as two healthy apps.

So a curl-based pinger would go green forever while every demo slept. This
loads each page the way a visitor does, which is the only check that cannot be
fooled, and is also the only thing guaranteed to actually wake an app.

Exit code is 0 if every demo ended up rendering, 1 if any could not be woken.
Apps found asleep are reported, not treated as failures -- being asleep is
Streamlit's normal free-tier behaviour, and the point of this job is that a
recruiter never meets it.
"""

from __future__ import annotations

import json
import sys
from datetime import UTC, datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

DEMOS = {
    "explainable-defect-detector": "https://explainable-defect-detector.streamlit.app/",
    "eu-ai-act-rag": "https://eu-ai-act-rag-eval.streamlit.app/",
    "ieee-fraud-ml": "https://ieee-fraud-ml.streamlit.app/",
    "rl-arm-reward-shaping": "https://rl-arm-reward-shaping.streamlit.app/",
    "vlm-hallucination-eval": "https://vlm-hallucination-eval.streamlit.app/",
}

WAKE_BUTTON = "text=Yes, get this app back up!"

# Streamlit Community Cloud serves a WRAPPER page and runs the real app inside
# an iframe titled "streamlitApp" (src .../~/+/). The wrapper is where the page
# title and the Zzzz screen live; the app's own DOM is only reachable through
# the frame. My first version waited for stAppViewContainer on the wrapper, so
# every app timed out at 180s while its title loaded perfectly - five green
# titles and five FAILED rows, which is exactly what a selector aimed at the
# wrong document looks like.
APP_FRAME = 'iframe[title="streamlitApp"]'
APP_READY = '[data-testid="stApp"]'
WAKE_TIMEOUT_MS = 120_000


def check(page, name: str, url: str) -> dict:
    t0 = datetime.now(UTC)
    row: dict = {"demo": name, "url": url, "was_asleep": False, "woken": False}

    page.goto(url, wait_until="domcontentloaded", timeout=60_000)
    try:
        page.wait_for_selector(WAKE_BUTTON, timeout=12_000)
        row["was_asleep"] = True
        page.click(WAKE_BUTTON)
    except Exception:
        pass  # not asleep, or it woke before we looked

    try:
        page.wait_for_selector(APP_FRAME, timeout=60_000)
        app = page.frame_locator(APP_FRAME).locator(APP_READY)
        app.wait_for(state="attached", timeout=WAKE_TIMEOUT_MS)
        # the container attaches before the first script run finishes
        page.wait_for_timeout(4_000)
        row["ok"] = True
        row["woken"] = row["was_asleep"]
        # prove the app rendered its own content, not just an empty container
        row["chars"] = len(page.frame_locator(APP_FRAME)
                           .locator("body").inner_text(timeout=20_000))
    except Exception as e:
        row["ok"] = False
        row["error"] = type(e).__name__

    row["seconds"] = round((datetime.now(UTC) - t0).total_seconds(), 1)
    row["title"] = page.title()
    return row


def main() -> int:
    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, url in DEMOS.items():
            ctx = browser.new_context()
            page = ctx.new_page()
            try:
                rows.append(check(page, name, url))
            except Exception as e:
                rows.append({"demo": name, "url": url, "ok": False,
                             "error": f"{type(e).__name__}: {e}"[:200]})
            ctx.close()
        browser.close()

    print(f"{'demo':30} {'status':>10} {'asleep?':>9} {'secs':>7}  "
          f"{'text':>12}  title")
    for r in rows:
        status = "ok" if r.get("ok") else "FAILED"
        asleep = "was asleep" if r.get("was_asleep") else "-"
        print(f"{r['demo']:30} {status:>10} {asleep:>9} "
              f"{r.get('seconds', 0):7.1f}  {r.get('chars', 0):>6} chars  "
              f"{r.get('title', '')[:34]}")

    woke = [r["demo"] for r in rows if r.get("was_asleep")]
    dead = [r["demo"] for r in rows if not r.get("ok")]
    if woke:
        print(f"\nwoke {len(woke)}: {', '.join(woke)}")
    if dead:
        print(f"\nCOULD NOT WAKE {len(dead)}: {', '.join(dead)}")

    out = Path(__file__).resolve().parents[1] / "reports"
    out.mkdir(exist_ok=True)
    (out / "demo_status.json").write_text(json.dumps(
        {"checked_at": datetime.now(UTC).isoformat(), "demos": rows}, indent=1))
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
