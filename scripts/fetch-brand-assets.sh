#!/usr/bin/env bash
# Downloads the real brand assets listed in the Reignite Brand Reference Pack
# into assets/brands/, using the exact source links and filenames from the pack.
# Nothing is redrawn, recoloured or generated: files are saved byte-for-byte.
set -u
cd "$(dirname "$0")/.."
UA="ReigniteBrandingReel/1.0 (asset fetch; contact: groupreignite)"

fetch() { # <dest> <url>
  mkdir -p "$(dirname "$1")"
  if [ -s "$1" ]; then echo "ok    $1 (already present)"; return; fi
  if curl -fsSL -A "$UA" -o "$1" "$2"; then echo "saved $1"; else echo "FAIL  $1  <-  $2"; rm -f "$1"; fi
}

B=assets/brands
fetch $B/01_Pepsi/Pepsi_2006.svg                     "https://upload.wikimedia.org/wikipedia/commons/5/5e/Pepsi_bi_%282006%29.svg"
fetch $B/01_Pepsi/Pepsi_2008.svg                     "https://upload.wikimedia.org/wikipedia/commons/e/e9/Pepsi_logo_2008.svg"
fetch $B/02_BBC/BBC_pre_1997.svg                     "https://upload.wikimedia.org/wikipedia/commons/7/7e/BBC_logo_%28pre97%29.svg"
fetch $B/02_BBC/BBC_1997.svg                         "https://upload.wikimedia.org/wikipedia/commons/5/5a/BBC_logo_%281997-2021%29.svg"
fetch $B/02_BBC/BBC_logo_evolution_reference.jpg     "https://cloudfront-us-east-1.images.arcpublishing.com/infobae/TBASD4XBTZAYXMGMSIBBKG7WFM.jpg"
fetch $B/03_Arthur_Andersen_Accenture/Arthur_Andersen_old.svg "https://upload.wikimedia.org/wikipedia/commons/7/7e/Arthur_Andersen_%28ancien%29.svg"
fetch $B/03_Arthur_Andersen_Accenture/Accenture.svg  "https://upload.wikimedia.org/wikipedia/commons/6/6f/Accenture.svg"
fetch $B/04_Coca_Cola/Coca_Cola_1946.svg             "https://upload.wikimedia.org/wikipedia/commons/c/ce/Coca-Cola_logo.svg"
fetch $B/05_Google/Google_2015.svg                   "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg"
fetch $B/05_Google/Google_evolution_reference.jpg    "https://static.tildacdn.biz/tild3963-3562-4936-b635-313635323361/Google-Logo-Design-E.jpg"

# The pack's Coca-Cola evolution link is a Pinterest *page*, not an image file.
CC=$B/04_Coca_Cola/Coca_Cola_evolution_reference.jpg
if [ ! -s "$CC" ]; then
  echo "MANUAL $CC"
  echo "       Open https://co.pinterest.com/pin/219057969373107801/ , save the image,"
  echo "       and place it at the path above (JPG)."
fi
