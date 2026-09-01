# verify

Everything in `reports/demo_status.json` came out of one program,
`scripts/ping_demos.py`, and nothing ever read it back. Most of that file is
measurement and cannot be rechecked offline, but three parts of it are not
measurements at all. They are derived from the measurements and from constants
in the script:

    thin  = chars < CONTENT_FLOOR
    woken = ok and was_asleep
    the demo names and urls = the DEMOS table in the script

Derived values are exactly the ones that go quietly wrong. If the threshold
moved, or a demo was renamed, or the file was hand edited or half written, the
report would still look perfectly ordinary. So the derived fields are
recomputed here from the raw ones, by two programs that share no code with the
script and no code with each other, and CI fails if they disagree with the file
or with each other.

## What each one recomputes

| Language | File | Recomputes | Result |
| --- | --- | --- | --- |
| Go | `gocheck/main.go` | Parses `DEMOS`, `CONTENT_FLOOR` and `ATTEMPTS` out of the script with regexes, then walks every `.json` under `reports/` and recomputes `thin`, `woken`, the url of every row, and the row/demo set. Also rejects a malformed, truncated or unknown-field document. | 1 file, 5 demos, `CONTENT_FLOOR=40`, `ATTEMPTS=2`, every derived field identical |
| SQL | `status.sql` | Same recomputation with sqlite's own JSON parser, over a demo table and constants that `verify.sh` extracts from the script with awk. So the script is parsed twice, by two different parsers, and the arithmetic is done twice. | no disagreeing rows |

Two implementations, not more. This repository publishes one small status file
and no computed results, so a third and fourth language would recompute the
same two comparisons again and prove nothing that these two do not already
prove. Padding the directory would make the checks look more serious than they
are, which is the opposite of the point.

## The checks have been seen to fail

A check nobody has watched reject anything is not a check. Eleven corruptions
were introduced one at a time and both implementations flagged all eleven,
independently:

    thin flipped on a 767 char row          chars lowered below the threshold
    woken flipped on a row that never slept  a url edited in the report
    attempts raised above ATTEMPTS           seconds set to zero
    the file truncated mid document          a demo row deleted
    a demo row duplicated                    CONTENT_FLOOR changed in the script
    a demo added to the script only

The CI job in `.github/workflows/verify.yml` repeats the smallest of these on
every push: it runs the checks, corrupts the file, requires rejection, restores
it and requires a pass.

## Running it

    ./verify/verify.sh

It prints `N passed, M failed, K skipped` and exits non-zero on any failure.
A missing toolchain is skipped with a message rather than counted as a pass.
