#!/usr/bin/env bash
# Recompute the derived fields of reports/demo_status.json independently of the
# script that wrote them, and fail if any two implementations disagree.
#
# Each check is skipped with a clear message if its toolchain is missing, so
# this runs on a laptop with only some of them. CI has both.
set -uo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

script=scripts/ping_demos.py
report=reports/demo_status.json
pass=0 fail=0 skip=0

run () {
    local name="$1" tool="$2"; shift 2
    printf '\n=== %s ===\n' "$name"
    if ! command -v "$tool" >/dev/null 2>&1; then
        printf 'skipped: %s is not installed\n' "$tool"
        skip=$((skip + 1)); return
    fi
    if "$@"; then pass=$((pass + 1)); else fail=$((fail + 1)); fi
}

check_go () { ( cd verify/gocheck && go run . -root "$root" ); }

# The SQL side needs the script's constants and its demo table. They are pulled
# out here with awk, which is a different parser from the regexes in the Go
# program, so the extraction is done twice as well as the arithmetic.
check_sql () {
    local prelude out floor attempts
    prelude="$(mktemp)" || return 1
    floor=$(awk -F'[ =]+' '/^CONTENT_FLOOR[ =]/ {print $2; exit}' "$script")
    attempts=$(awk -F'[ =]+' '/^ATTEMPTS[ =]/ {print $2; exit}' "$script")
    case "$floor$attempts" in
        ''|*[!0-9]*) echo "could not read CONTENT_FLOOR/ATTEMPTS from $script"
                     rm -f "$prelude"; return 1 ;;
    esac

    {
        echo "CREATE TEMP TABLE consts(floor INT, attempts INT);"
        echo "INSERT INTO consts VALUES($floor, $attempts);"
        echo "CREATE TEMP TABLE script_demos(name TEXT, url TEXT);"
        awk '/^DEMOS[ =]/ {inside=1; next}
             inside && /^}/ {inside=0}
             inside && match($0, /"[^"]+"[ ]*:[ ]*"[^"]+"/) {
                 s = substr($0, RSTART, RLENGTH)
                 split(s, p, /"[ ]*:[ ]*"/)
                 gsub(/^[ ]*"/, "", p[1]); gsub(/"$/, "", p[2])
                 printf "INSERT INTO script_demos VALUES(%c%s%c, %c%s%c);\n", \
                        39, p[1], 39, 39, p[2], 39
             }' "$script"
    } > "$prelude"

    if ! grep -q 'INSERT INTO script_demos' "$prelude"; then
        echo "could not read the DEMOS table from $script"
        rm -f "$prelude"; return 1
    fi

    # sqlite3 reads stdin, which inside a script is the script itself, so the
    # redirect is not optional.
    out=$(sqlite3 :memory: ".read $prelude" ".read verify/status.sql" \
          < /dev/null 2>&1 | tr -d '\r')
    rm -f "$prelude"
    if [ -n "$out" ]; then
        echo "SQL disagrees with $report:"
        echo "$out"
        return 1
    fi
    echo "SQL: thin, woken, attempts and every url agree (CONTENT_FLOOR=$floor, ATTEMPTS=$attempts)"
    return 0
}

run "Go, structure and derived fields" go      check_go
run "SQL, derived fields again"        sqlite3 check_sql

printf '\n%s\n' "----------------------------------------"
printf '%d passed, %d failed, %d skipped\n' "$pass" "$fail" "$skip"
[ "$fail" -eq 0 ] || exit 1
[ "$pass" -gt 0 ] || { echo "nothing ran"; exit 1; }
