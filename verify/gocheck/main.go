// Structural validation of reports/demo_status.json, plus an independent
// recomputation of every field in it that ping_demos.py derives rather than
// measures.
//
// reports/demo_status.json is the only data file this repository publishes. It
// is written by scripts/ping_demos.py and nothing ever read it back. Three of
// its fields are not measurements at all, they are derived from the
// measurements and from constants in the script:
//
//	thin  = chars < CONTENT_FLOOR
//	woken = ok and was_asleep
//	the demo/url set = the DEMOS table in the script
//
// So they can be recomputed here from the raw fields, by a program that shares
// no code with the one that wrote them. A wrong threshold, a stale demo list,
// a truncated write or a hand edit all show up as a disagreement.
//
// Run: cd verify/gocheck && go run . -root ../..
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"time"
)

type row struct {
	Demo      *string  `json:"demo"`
	URL       *string  `json:"url"`
	WasAsleep *bool    `json:"was_asleep"`
	Woken     *bool    `json:"woken"`
	OK        *bool    `json:"ok"`
	Chars     *int     `json:"chars"`
	Thin      *bool    `json:"thin"`
	Seconds   *float64 `json:"seconds"`
	Attempts  *int     `json:"attempts"`
	Title     *string  `json:"title"`
	Error     *string  `json:"error"`
}

type status struct {
	CheckedAt *string `json:"checked_at"`
	Demos     []row   `json:"demos"`
}

// Constants and the demo table, read out of the script's source. Parsed rather
// than copied: a copy drifts the moment someone edits the script, and then the
// check quietly measures nothing.
type script struct {
	demos        map[string]string
	contentFloor int
	attempts     int
}

var (
	reDemosBlock = regexp.MustCompile(`(?s)\nDEMOS\s*=\s*\{(.*?)\n\}`)
	reDemoEntry  = regexp.MustCompile(`"([^"]+)"\s*:\s*"([^"]+)"`)
	reFloor      = regexp.MustCompile(`\nCONTENT_FLOOR\s*=\s*(\d+)`)
	reAttempts   = regexp.MustCompile(`\nATTEMPTS\s*=\s*(\d+)`)
)

func parseScript(path string) (script, error) {
	var s script
	b, err := os.ReadFile(path)
	if err != nil {
		return s, err
	}
	src := string(b)

	block := reDemosBlock.FindStringSubmatch(src)
	if block == nil {
		return s, fmt.Errorf("no DEMOS = { ... } table in %s", path)
	}
	s.demos = map[string]string{}
	for _, m := range reDemoEntry.FindAllStringSubmatch(block[1], -1) {
		if _, dup := s.demos[m[1]]; dup {
			return s, fmt.Errorf("demo %q listed twice in DEMOS", m[1])
		}
		s.demos[m[1]] = m[2]
	}
	if len(s.demos) == 0 {
		return s, fmt.Errorf("DEMOS table in %s is empty", path)
	}

	for _, spec := range []struct {
		re   *regexp.Regexp
		name string
		dst  *int
	}{
		{reFloor, "CONTENT_FLOOR", &s.contentFloor},
		{reAttempts, "ATTEMPTS", &s.attempts},
	} {
		m := spec.re.FindStringSubmatch(src)
		if m == nil {
			return s, fmt.Errorf("no %s in %s", spec.name, path)
		}
		v, err := strconv.Atoi(m[1])
		if err != nil || v <= 0 {
			return s, fmt.Errorf("%s is not a positive integer", spec.name)
		}
		*spec.dst = v
	}
	return s, nil
}

type report struct{ problems []string }

func (r *report) bad(format string, a ...any) {
	r.problems = append(r.problems, fmt.Sprintf(format, a...))
}

func (r *report) checkStatus(st status, s script, path string) {
	if st.CheckedAt == nil {
		r.bad("%s: no checked_at", path)
	} else if _, err := time.Parse(time.RFC3339, *st.CheckedAt); err != nil {
		r.bad("%s: checked_at %q is not RFC3339", path, *st.CheckedAt)
	}
	if len(st.Demos) == 0 {
		r.bad("%s: no demo rows", path)
		return
	}

	seen := map[string]bool{}
	for i, d := range st.Demos {
		where := fmt.Sprintf("%s row %d", path, i)
		if d.Demo == nil || *d.Demo == "" {
			r.bad("%s: no demo name", where)
			continue
		}
		name := *d.Demo
		where = fmt.Sprintf("%s row %q", path, name)
		if seen[name] {
			r.bad("%s: listed twice", where)
			continue
		}
		seen[name] = true

		wantURL, known := s.demos[name]
		if !known {
			r.bad("%s: not in the DEMOS table of the script", where)
		} else if d.URL == nil || *d.URL != wantURL {
			r.bad("%s: url disagrees with the script", where)
		}

		if d.OK == nil {
			r.bad("%s: no ok field", where)
			continue
		}
		if d.WasAsleep == nil {
			r.bad("%s: no was_asleep field", where)
			continue
		}
		if d.Attempts == nil || *d.Attempts < 1 || *d.Attempts > s.attempts {
			r.bad("%s: attempts outside 1..%d", where, s.attempts)
		}

		// woken is derived: the script sets it only on the success path.
		wantWoken := *d.OK && *d.WasAsleep
		if d.Woken == nil || *d.Woken != wantWoken {
			r.bad("%s: woken should be %v (ok=%v, was_asleep=%v)",
				where, wantWoken, *d.OK, *d.WasAsleep)
		}

		if *d.OK {
			if d.Chars == nil || *d.Chars < 0 {
				r.bad("%s: ok row without a chars count", where)
				continue
			}
			// thin is derived from chars and the script's own threshold.
			wantThin := *d.Chars < s.contentFloor
			if d.Thin == nil || *d.Thin != wantThin {
				r.bad("%s: thin should be %v (chars=%d, CONTENT_FLOOR=%d)",
					where, wantThin, *d.Chars, s.contentFloor)
			}
			if d.Seconds == nil || *d.Seconds <= 0 {
				r.bad("%s: ok row without a positive elapsed time", where)
			}
		} else if d.Error == nil || *d.Error == "" {
			r.bad("%s: failed row with no error recorded", where)
		}
	}

	var missing []string
	for name := range s.demos {
		if !seen[name] {
			missing = append(missing, name)
		}
	}
	sort.Strings(missing)
	if len(missing) > 0 {
		r.bad("%s: the script pings %s but the report has no row for them",
			path, strings.Join(missing, ", "))
	}
}

func main() {
	root := flag.String("root", ".", "repository root")
	flag.Parse()

	s, err := parseScript(filepath.Join(*root, "scripts", "ping_demos.py"))
	if err != nil {
		fmt.Println("FAIL", err)
		os.Exit(1)
	}

	r := &report{}
	files := 0
	err = filepath.Walk(filepath.Join(*root, "reports"), func(p string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if info.IsDir() || filepath.Ext(p) != ".json" {
			return nil
		}
		files++
		rel, _ := filepath.Rel(*root, p)
		b, err := os.ReadFile(p)
		if err != nil {
			r.bad("%s: %v", rel, err)
			return nil
		}
		// encoding/json rejects NaN, Infinity, trailing garbage and truncation
		// outright, which is most of what a bad write looks like.
		var st status
		dec := json.NewDecoder(strings.NewReader(string(b)))
		dec.DisallowUnknownFields()
		if err := dec.Decode(&st); err != nil {
			r.bad("%s: %v", rel, err)
			return nil
		}
		if dec.More() {
			r.bad("%s: trailing content after the JSON document", rel)
			return nil
		}
		r.checkStatus(st, s, rel)
		return nil
	})
	if err != nil {
		fmt.Println("FAIL", err)
		os.Exit(1)
	}
	if files == 0 {
		fmt.Println("FAIL no .json files under reports/")
		os.Exit(1)
	}

	if len(r.problems) > 0 {
		fmt.Printf("FAIL %d problem(s):\n", len(r.problems))
		for _, p := range r.problems {
			fmt.Println("  -", p)
		}
		os.Exit(1)
	}
	fmt.Printf("Go: %d report file(s), %d demo(s), CONTENT_FLOOR=%d, ATTEMPTS=%d; "+
		"thin, woken and every url recomputed and identical\n",
		files, len(s.demos), s.contentFloor, s.attempts)
}
