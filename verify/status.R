# Recompute derived fields of reports/demo_status.json in R.
#
# Uses only base R -- no jsonlite. Parses the JSON with a line-by-line scanner,
# reads the script constants from scripts/ping_demos.py, and checks
# thin/woken/url/attempts against the raw measurements.
#
# Run: Rscript verify/status.R <repo root>

args <- commandArgs(trailingOnly = TRUE)
root <- if (length(args) > 0) args[1] else "."

script_text <- paste(readLines(file.path(root, "scripts", "ping_demos.py"),
                               warn = FALSE), collapse = "\n")

floor_val    <- as.integer(sub(".*\nCONTENT_FLOOR\\s*=\\s*(\\d+).*", "\\1", script_text))
attempts_val <- as.integer(sub(".*\nATTEMPTS\\s*=\\s*(\\d+).*", "\\1", script_text))

demos_block <- regmatches(script_text,
                          regexpr("(?s)\nDEMOS\\s*=\\s*\\{.*?\n\\}", script_text, perl = TRUE))
pairs <- regmatches(demos_block,
                    gregexpr('"([^"]+)"\\s*:\\s*"([^"]+)"', demos_block, perl = TRUE))[[1]]
demo_names <- sub('^"([^"]+)"\\s*:.*', "\\1", pairs)
demo_urls  <- sub('.*:\\s*"([^"]+)"$', "\\1", pairs)
names(demo_urls) <- demo_names

# Minimal JSON object parser for the flat demo_status.json structure.
# Walks the file character by character -- no external library.
json_text <- paste(readLines(file.path(root, "reports", "demo_status.json"),
                             warn = FALSE), collapse = "\n")

# Use R's built-in JSON parsing via the pipe to python... no, let's just
# use a regex approach on the known structure.
# Each demo object is { "demo": "...", "url": "...", ... }

# Extract each demo object as a substring
obj_starts <- gregexpr("\\{[^{}]*\\}", json_text, perl = TRUE)[[1]]
obj_texts <- regmatches(json_text, list(obj_starts))[[1]]

# But the top-level object also matches -- filter to only those with "demo" key
demo_objs <- obj_texts[grepl('"demo"', obj_texts)]

extract_str <- function(obj, key) {
  pat <- paste0('"', key, '"\\s*:\\s*"([^"]*)"')
  m <- regmatches(obj, regexpr(pat, obj, perl = TRUE))
  if (length(m) == 0 || nchar(m) == 0) return(NA_character_)
  sub(pat, "\\1", m, perl = TRUE)
}

extract_num <- function(obj, key) {
  pat <- paste0('"', key, '"\\s*:\\s*([0-9.eE+-]+)')
  m <- regmatches(obj, regexpr(pat, obj, perl = TRUE))
  if (length(m) == 0 || nchar(m) == 0) return(NA_real_)
  as.numeric(sub(pat, "\\1", m, perl = TRUE))
}

extract_bool <- function(obj, key) {
  pat <- paste0('"', key, '"\\s*:\\s*(true|false)')
  m <- regmatches(obj, regexpr(pat, obj, perl = TRUE))
  if (length(m) == 0 || nchar(m) == 0) return(NA)
  sub(pat, "\\1", m, perl = TRUE) == "true"
}

bad <- 0
fail <- function(msg) { cat("  FAIL:", msg, "\n"); bad <<- bad + 1 }

seen <- character(0)
for (obj in demo_objs) {
  name     <- extract_str(obj, "demo")
  url      <- extract_str(obj, "url")
  ok       <- extract_bool(obj, "ok")
  was_asl  <- extract_bool(obj, "was_asleep")
  woken    <- extract_bool(obj, "woken")
  thin     <- extract_bool(obj, "thin")
  chars    <- extract_num(obj, "chars")
  seconds  <- extract_num(obj, "seconds")
  att      <- extract_num(obj, "attempts")

  if (is.na(name)) next
  seen <- c(seen, name)

  want_woken <- isTRUE(ok) && isTRUE(was_asl)
  if (!identical(woken, want_woken))
    fail(paste0(name, ": woken should be ", want_woken))

  if (isTRUE(ok)) {
    want_thin <- chars < floor_val
    if (!identical(thin, want_thin))
      fail(paste0(name, ": thin should be ", want_thin))
    if (is.na(seconds) || seconds <= 0)
      fail(paste0(name, ": ok row without positive seconds"))
  }

  if (is.na(att) || att < 1 || att > attempts_val)
    fail(paste0(name, ": attempts outside 1..", attempts_val))

  if (name %in% names(demo_urls) && url != unname(demo_urls[name]))
    fail(paste0(name, ": url disagrees with script"))
}

for (d in demo_names) {
  if (!(d %in% seen)) fail(paste0(d, ": in script but absent from report"))
}

if (bad > 0) {
  cat("R:", bad, "problem(s)\n")
  quit(status = 1)
}
cat("R:", length(seen), "demo(s), thin/woken/url recomputed, CONTENT_FLOOR=",
    floor_val, ", ATTEMPTS=", attempts_val, "\n", sep = "")
