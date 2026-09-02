/* Recompute the derived fields of reports/demo_status.json in C.
 *
 * Reads the script constants (CONTENT_FLOOR, ATTEMPTS) and the DEMOS table
 * from scripts/ping_demos.py with its own parser, then walks the JSON report
 * and checks every derived field against the raw measurements.
 *
 * Build: cc -std=c99 -O2 -Wall -o statusc verify/status.c -lm
 * Run:   ./statusc <repo root>
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_DEMOS 32
#define BUFSZ (1 << 18)

static int problems = 0;
static void fail(const char *msg) { printf("  FAIL: %s\n", msg); problems++; }

static char *slurp(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) return NULL;
    fseek(f, 0, SEEK_END);
    long n = ftell(f);
    rewind(f);
    char *b = malloc((size_t)n + 1);
    fread(b, 1, (size_t)n, f);
    b[n] = '\0';
    fclose(f);
    return b;
}

typedef struct { char name[128]; char url[256]; } demo_entry;

static int parse_int_const(const char *src, const char *name) {
    char pat[64];
    snprintf(pat, sizeof pat, "\n%s", name);
    const char *p = strstr(src, pat);
    if (!p) { fprintf(stderr, "no %s in script\n", name); exit(1); }
    p += strlen(pat);
    while (*p == ' ' || *p == '=') p++;
    return atoi(p);
}

static int parse_demos(const char *src, demo_entry *out) {
    const char *p = strstr(src, "\nDEMOS");
    if (!p) { fprintf(stderr, "no DEMOS table\n"); exit(1); }
    p = strchr(p, '{');
    if (!p) { fprintf(stderr, "no { after DEMOS\n"); exit(1); }
    const char *end = strchr(p, '}');
    if (!end) end = src + strlen(src);
    int n = 0;
    while (p < end && n < MAX_DEMOS) {
        p = strchr(p, '"');
        if (!p || p >= end) break;
        p++;
        char *q = out[n].name;
        while (*p && *p != '"') *q++ = *p++;
        *q = '\0';
        if (*p == '"') p++;
        p = strchr(p, '"');
        if (!p || p >= end) break;
        p++;
        q = out[n].url;
        while (*p && *p != '"') *q++ = *p++;
        *q = '\0';
        if (*p == '"') p++;
        n++;
    }
    return n;
}

/* Tiny JSON helpers -- good enough for this structure. */
static const char *find_key(const char *j, const char *key) {
    char pat[128];
    snprintf(pat, sizeof pat, "\"%s\"", key);
    const char *p = strstr(j, pat);
    if (!p) return NULL;
    p += strlen(pat);
    while (*p == ' ' || *p == ':' || *p == '\t' || *p == '\n' || *p == '\r') p++;
    return p;
}

static int json_bool(const char *p) {
    if (!p) return -1;
    if (strncmp(p, "true", 4) == 0) return 1;
    if (strncmp(p, "false", 5) == 0) return 0;
    return -1;
}

static int json_int(const char *p) {
    if (!p) return -999999;
    if (*p == '-' || (*p >= '0' && *p <= '9')) return atoi(p);
    return -999999;
}

static double json_double(const char *p) {
    if (!p) return -1.0;
    return atof(p);
}

/* Extract the value of a key inside one demo object (bounded search). */
static const char *obj_key(const char *start, const char *obj_end, const char *key) {
    char pat[128];
    snprintf(pat, sizeof pat, "\"%s\"", key);
    const char *p = start;
    while ((p = strstr(p, pat)) != NULL && p < obj_end) {
        p += strlen(pat);
        while (*p == ' ' || *p == ':' || *p == '\t' || *p == '\n' || *p == '\r') p++;
        return p;
    }
    return NULL;
}

int main(int argc, char **argv) {
    const char *root = argc > 1 ? argv[1] : ".";
    char path[512];

    snprintf(path, sizeof path, "%s/scripts/ping_demos.py", root);
    char *script = slurp(path);
    if (!script) { fprintf(stderr, "cannot read %s\n", path); return 1; }

    int floor_val = parse_int_const(script, "CONTENT_FLOOR");
    int attempts_val = parse_int_const(script, "ATTEMPTS");
    demo_entry demos[MAX_DEMOS];
    int ndemos = parse_demos(script, demos);
    free(script);

    snprintf(path, sizeof path, "%s/reports/demo_status.json", root);
    char *json = slurp(path);
    if (!json) { fprintf(stderr, "cannot read %s\n", path); return 1; }

    const char *arr = find_key(json, "demos");
    if (!arr || *arr != '[') { fprintf(stderr, "no demos array\n"); return 1; }

    int checked = 0;
    int seen[MAX_DEMOS];
    memset(seen, 0, sizeof seen);

    const char *p = arr + 1;
    while (*p) {
        while (*p && *p != '{' && *p != ']') p++;
        if (*p != '{') break;
        const char *obj_start = p;
        int depth = 1;
        p++;
        while (*p && depth > 0) {
            if (*p == '{') depth++;
            else if (*p == '}') depth--;
            p++;
        }
        const char *obj_end = p;
        checked++;

        const char *v;
        char demo_name[128] = {0};
        v = obj_key(obj_start, obj_end, "demo");
        if (v && *v == '"') {
            const char *s = v + 1;
            int i = 0;
            while (*s && *s != '"' && i < 127) demo_name[i++] = *s++;
            demo_name[i] = '\0';
        }

        int ok_val   = json_bool(obj_key(obj_start, obj_end, "ok"));
        int was_val  = json_bool(obj_key(obj_start, obj_end, "was_asleep"));
        int woken_v  = json_bool(obj_key(obj_start, obj_end, "woken"));
        int thin_v   = json_bool(obj_key(obj_start, obj_end, "thin"));
        int chars_v  = json_int(obj_key(obj_start, obj_end, "chars"));
        int att_v    = json_int(obj_key(obj_start, obj_end, "attempts"));
        double sec_v = json_double(obj_key(obj_start, obj_end, "seconds"));

        int want_woken = (ok_val == 1 && was_val == 1) ? 1 : 0;
        if (woken_v != want_woken) {
            char msg[256];
            snprintf(msg, sizeof msg, "%s: woken should be %d", demo_name, want_woken);
            fail(msg);
        }

        if (ok_val == 1) {
            int want_thin = (chars_v < floor_val) ? 1 : 0;
            if (thin_v != want_thin) {
                char msg[256];
                snprintf(msg, sizeof msg, "%s: thin should be %d (chars=%d, floor=%d)",
                         demo_name, want_thin, chars_v, floor_val);
                fail(msg);
            }
            if (sec_v <= 0) {
                char msg[256];
                snprintf(msg, sizeof msg, "%s: ok row without positive seconds", demo_name);
                fail(msg);
            }
        }

        if (att_v < 1 || att_v > attempts_val) {
            char msg[256];
            snprintf(msg, sizeof msg, "%s: attempts %d outside 1..%d",
                     demo_name, att_v, attempts_val);
            fail(msg);
        }

        /* Mark this demo as seen and check its URL against the script. */
        for (int i = 0; i < ndemos; i++) {
            if (strcmp(demos[i].name, demo_name) == 0) {
                seen[i] = 1;
                v = obj_key(obj_start, obj_end, "url");
                if (v && *v == '"') {
                    char url_buf[256] = {0};
                    const char *s = v + 1;
                    int j = 0;
                    while (*s && *s != '"' && j < 255) url_buf[j++] = *s++;
                    url_buf[j] = '\0';
                    if (strcmp(url_buf, demos[i].url) != 0) {
                        char msg[512];
                        snprintf(msg, sizeof msg, "%s: url disagrees with script", demo_name);
                        fail(msg);
                    }
                }
                break;
            }
        }
    }

    for (int i = 0; i < ndemos; i++) {
        if (!seen[i]) {
            char msg[256];
            snprintf(msg, sizeof msg, "%s: in the script but absent from the report", demos[i].name);
            fail(msg);
        }
    }

    free(json);
    if (problems) {
        printf("C: %d problem(s)\n", problems);
        return 1;
    }
    printf("C: %d demo(s), thin/woken/url recomputed, CONTENT_FLOOR=%d, ATTEMPTS=%d\n",
           checked, floor_val, attempts_val);
    return 0;
}
