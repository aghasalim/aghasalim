# scripts

`check_claims.py.disabled` reads the figures quoted on the profile and verifies
each one against the repository it came from, failing if they drift apart. It ran
in CI until the profile stopped quoting figures.

It is kept, and disabled rather than deleted, because it is the right tool the
moment the profile makes a numeric claim again. Running it against a profile with
no claims reports "no linked project sections found" and exits 1, which is
deliberate: a checker that silently passes while verifying nothing is worse than
one that breaks loudly.

To bring it back: rename it to `check_claims.py`, restore
`.github/workflows/check-claims.yml`, and make sure each project line keeps the
`**[Name](repo-url)**` shape on a single line, since that is what pairs a
repository with the figures beside it.
