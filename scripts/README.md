# scripts

`ping_demos.py` keeps the Streamlit demos awake. It drives a real browser rather
than curl, because a sleeping app serves the same HTTP 303 and the same HTML
shell as a running one and curl cannot tell them apart.

`check_claims.py.disabled` reads the figures quoted on the profile and checks
each against the repository it came from, failing when they drift apart. It ran
in CI while the profile quoted figures. The profile no longer does, so it has
nothing to verify: it reports "no linked project sections found" and exits 1,
which is deliberate. A checker that silently passes while verifying nothing is
worse than one that breaks loudly, and leaving it running would mean a
permanently red badge for a check doing its job.

To bring it back: rename it to `check_claims.py`, restore
`.github/workflows/check-claims.yml`, and keep each project line in the
`**[Name](repo-url)**` shape on a single line, since that is what pairs a
repository with the figures beside it.

`verify/` recomputes the derived fields of `reports/demo_status.json` from the
raw ones, in Go and in SQL, and CI fails if either disagrees with what
`ping_demos.py` wrote. See `verify/README.md`.
