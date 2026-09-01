-- Second, independent recomputation of the derived fields in
-- reports/demo_status.json.
--
-- verify/gocheck does this in Go. This does it again in SQL, reading the JSON
-- with sqlite's own parser and taking the script's constants from a prelude
-- that verify/verify.sh builds with awk. So the demo table and the thresholds
-- are extracted twice, by two different parsers, and the derived fields are
-- recomputed twice from the raw ones. A mistake in either parser shows up as a
-- disagreement rather than as a check that quietly passes.
--
-- Expects, from the prelude: script_demos(name, url) and consts(floor, attempts).
-- Prints one line per problem and nothing at all when the file is consistent.
-- Run: see verify/verify.sh

.mode list
.headers off

CREATE TEMP VIEW rows_ AS
SELECT json_extract(value, '$.demo')       AS demo,
       json_extract(value, '$.url')        AS url,
       json_extract(value, '$.ok')         AS ok,
       json_extract(value, '$.was_asleep') AS was_asleep,
       json_extract(value, '$.woken')      AS woken,
       json_extract(value, '$.thin')       AS thin,
       json_extract(value, '$.chars')      AS chars,
       json_extract(value, '$.seconds')    AS seconds,
       json_extract(value, '$.attempts')   AS attempts
FROM json_each(readfile('reports/demo_status.json'), '$.demos');

SELECT 'row ' || demo || ': thin should be ' || (chars < (SELECT floor FROM consts))
FROM rows_ WHERE ok = 1 AND thin IS NOT (chars < (SELECT floor FROM consts));

SELECT 'row ' || demo || ': woken should be ' || (ok = 1 AND was_asleep = 1)
FROM rows_ WHERE woken IS NOT (ok = 1 AND was_asleep = 1);

SELECT 'row ' || demo || ': attempts outside 1..' || (SELECT attempts FROM consts)
FROM rows_ WHERE attempts IS NULL
   OR attempts < 1 OR attempts > (SELECT attempts FROM consts);

SELECT 'row ' || demo || ': ok row without a positive elapsed time'
FROM rows_ WHERE ok = 1 AND (seconds IS NULL OR seconds <= 0);

SELECT 'row ' || demo || ': listed twice'
FROM rows_ GROUP BY demo HAVING count(*) > 1;

-- The report and the script must describe the same set of demos at the same
-- urls. A full outer join by hand, because sqlite has no FULL JOIN here.
SELECT 'row ' || r.demo || ': url disagrees with the script'
FROM rows_ r JOIN script_demos s ON s.name = r.demo WHERE s.url IS NOT r.url;

SELECT 'row ' || demo || ': not in the DEMOS table of the script'
FROM rows_ WHERE demo NOT IN (SELECT name FROM script_demos);

SELECT 'demo ' || name || ': in the script but absent from the report'
FROM script_demos WHERE name NOT IN (SELECT demo FROM rows_);

SELECT 'the report has no demo rows' WHERE (SELECT count(*) FROM rows_) = 0;

SELECT 'checked_at is not a timestamp sqlite can read'
WHERE julianday(json_extract(readfile('reports/demo_status.json'),
                             '$.checked_at')) IS NULL;
