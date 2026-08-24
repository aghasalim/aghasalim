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

# Clicking the wake button replaces the Zzzz screen with a "spinning up" screen,
# and the streamlitApp iframe does not exist during it. On a cold wake that gap
# ran past the 60s I first allowed here: the 2026-08-22 run failed eu-ai-act-rag
# at exactly 63.0s, which is goto + the 12s Zzzz probe + a 60s frame wait that
# expired. The app was healthy the whole time. A woken app therefore gets the
# full wake budget to produce its frame, and a warm one keeps the short wait.
FRAME_TIMEOUT_WARM_MS = 60_000
ATTEMPTS = 2

# Content settle: poll up to 24s for the app to paint something.
SETTLE_STEP_MS = 3_000
SETTLE_POLLS = 8
CONTENT_FLOOR = 40


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
        frame_timeout = WAKE_TIMEOUT_MS if row["was_asleep"] else FRAME_TIMEOUT_WARM_MS
        page.wait_for_selector(APP_FRAME, timeout=frame_timeout)
        app = page.frame_locator(APP_FRAME).locator(APP_READY)
        app.wait_for(state="attached", timeout=WAKE_TIMEOUT_MS)
        # The container attaches well before the first script run paints. A flat
        # 4s wait was not enough: the 2026-08-24 run passed
        # explainable-defect-detector at 9 chars with the generic "Streamlit"
        # title, i.e. an empty shell scored as healthy. Poll instead, and stop as
        # soon as there is real text rather than always paying the full budget.
        body = page.frame_locator(APP_FRAME).locator("body")
        chars = 0
        for _ in range(SETTLE_POLLS):
            page.wait_for_timeout(SETTLE_STEP_MS)
            chars = len(body.inner_text(timeout=20_000))
            if chars >= CONTENT_FLOOR:
                break
        row["ok"] = True
        row["woken"] = row["was_asleep"]
        row["chars"] = chars
        # Not a failure: some demos legitimately render very little above the
        # fold. It is flagged so a genuinely blank wake is visible instead of
        # sitting behind a green tick.
        row["thin"] = chars < CONTENT_FLOOR
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
            # Waking is racy by nature, so one failure is not yet a dead demo.
            # Each attempt gets a clean context; the second starts against an
            # app the first has already nudged awake.
            for attempt in range(1, ATTEMPTS + 1):
                ctx = browser.new_context()
                page = ctx.new_page()
                try:
                    row = check(page, name, url)
                except Exception as e:
                    row = {"demo": name, "url": url, "ok": False,
                           "error": f"{type(e).__name__}: {e}"[:200]}
                ctx.close()
                row["attempts"] = attempt
                if row.get("ok") or attempt == ATTEMPTS:
                    rows.append(row)
                    break
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
    thin = [r["demo"] for r in rows if r.get("ok") and r.get("thin")]
    if woke:
        print(f"\nwoke {len(woke)}: {', '.join(woke)}")
    if thin:
        print(f"\nTHIN (rendered under {CONTENT_FLOOR} chars, check by hand): "
              f"{', '.join(thin)}")
    if dead:
        print(f"\nCOULD NOT WAKE {len(dead)}: {', '.join(dead)}")

    out = Path(__file__).resolve().parents[1] / "reports"
    out.mkdir(exist_ok=True)
    (out / "demo_status.json").write_text(json.dumps(
        {"checked_at": datetime.now(UTC).isoformat(), "demos": rows}, indent=1))
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
