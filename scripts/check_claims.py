"""Fail if a figure quoted on this profile no longer appears in its source repo.

Why this exists: the RAG project was re-evaluated after a truncation bug was
found, and this README kept quoting the superseded numbers for a while. Anyone
clicking through from the profile into the repo would have found two different
sets of numbers for the same experiment -- which is worse than either number on
its own.

Drift is caused by the *project* changing, not by this file changing, so the
workflow runs on a schedule as well as on push.

What it checks, and what it deliberately does not
-------------------------------------------------
Only distinctive figures: percentages carrying a decimal (`90.2%`) and bare
decimals (`0.795`, `0.9874`). Those are exactly the values that move when a
result is recomputed.

Plain integers are ignored on purpose. "45 questions" might legitimately appear
in the source as "45 hand-written", "12 out of 12" as "12/12", and asserting on
those produces noise that trains you to ignore the check -- which is worse than
having no check at all.
"""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "README.md"
OWNER = "aghasalim"
# Docs in the source repo that may legitimately hold the figure.
SOURCES = ["README.md", "RESULTS.md", "NOTES.md"]

REPO_LINK = re.compile(rf"https://github\.com/{OWNER}/([A-Za-z0-9._-]+)")
# This repo links to itself (the badge). Left in, the intro would be "verified"
# against the very file the figures were read from, which always passes and
# therefore checks nothing.
SELF = OWNER
# A percentage with a decimal, or a bare 0.xxx / n.xxx decimal.
FIGURE = re.compile(r"\b\d{1,3}\.\d+%|\b\d\.\d{3,4}\b")

# Figures that are genuinely profile-only. Keep this short and justified: every
# entry is a place the check has been told to stop looking, so an unexplained
# one is how real drift eventually slips through.
ALLOW: dict[str, set[str]] = {
    # Prose rounding of the repo's 3.499% fraud rate. Rounding is not drift, and
    # "3.499% fraud" reads badly in a sentence.
    "ieee-fraud-ml": {"3.5%"},
}


def fetch(repo: str, path: str) -> str:
    for branch in ("main", "master"):
        url = f"https://raw.githubusercontent.com/{OWNER}/{repo}/{branch}/{path}"
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                continue
            raise
        except urllib.error.URLError:
            continue
    return ""


def sections(text: str) -> list[tuple[str, str]]:
    """Split the profile into project blocks keyed by their linked repo.

    Two kinds of block, because the profile quotes figures in two places:

    * a row of the index table, which links exactly one repo;
    * a prose write-up, introduced by a bold title followed by a middot.

    Table rows are pulled out *first* and excluded from the prose split. Left in,
    the whole table would fall into the leading part, `REPO_LINK.search` would
    match whichever repo is listed first, and every figure in the index would be
    checked against that one project -- reporting drift for ten repos whose
    numbers are fine.
    """
    # A one-line entry is a third kind of block, and the one the profile now
    # uses: "**[Name](repo-url)** — finding". It is exactly a table row without
    # the pipes, so it is collected the same way. Added after the profile
    # dropped its tables and this parser reported "no linked project sections
    # found" -- a checker that silently verifies nothing is worse than a broken
    # one, so it fails loudly and this keeps it fed.
    table_rows, prose_lines = [], []
    for line in text.splitlines():
        # Drop a leading markdown bullet ("- ", "* ", "+ ") before testing shape,
        # so a bulleted one-liner "- **[Name](url)** — finding" is recognised the
        # same as an unbulleted one. Added when the profile moved its selected
        # work into a bullet list and this parser stopped seeing any project
        # block at all -- a checker that verifies nothing must fail loud, and did.
        stripped = re.sub(r"^[-*+]\s+", "", line.lstrip())
        one_liner = stripped.startswith("**[") and REPO_LINK.search(line)
        if (stripped.startswith("|") or one_liner) and REPO_LINK.search(line):
            table_rows.append(line)
        else:
            prose_lines.append(line)

    out = []
    for row in table_rows:
        m = REPO_LINK.search(row)
        if m and m.group(1) != SELF:
            out.append((m.group(1), row))
    for p in re.split(r"\n(?=\*\*[^*\n]+\*\*\s*·)", "\n".join(prose_lines)):
        m = REPO_LINK.search(p)
        if m and m.group(1) != SELF:
            out.append((m.group(1), p))
    return out


def main() -> int:
    profile = PROFILE.read_text(encoding="utf-8")
    blocks = sections(profile)
    if not blocks:
        print("no linked project sections found -- check the parser")
        return 1

    failures, checked = [], 0
    for repo, block in blocks:
        figures = sorted(set(FIGURE.findall(block)) - ALLOW.get(repo, set()))
        if not figures:
            print(f"  {repo}: no distinctive figures quoted")
            continue

        corpus = "\n".join(fetch(repo, p) for p in SOURCES)
        if not corpus.strip():
            failures.append(f"{repo}: could not fetch any of {SOURCES}")
            continue

        missing = [f for f in figures if f not in corpus]
        checked += len(figures)
        status = "OK " if not missing else "FAIL"
        print(f"  {status} {repo}: {len(figures)-len(missing)}/{len(figures)} figures match")
        for f in missing:
            failures.append(f"{repo}: profile quotes {f}, absent from {'/'.join(SOURCES)}")

    print(f"\nchecked {checked} figures across {len(blocks)} projects")
    if failures:
        print("\nDRIFT DETECTED:")
        for f in failures:
            print(f"  - {f}")
        print("\nThe profile and the source repo disagree. Fix whichever is stale;\n"
              "if the figure is legitimately profile-only, add it to ALLOW with a reason.")
        return 1
    print("no drift")
    return 0


if __name__ == "__main__":
    sys.exit(main())
