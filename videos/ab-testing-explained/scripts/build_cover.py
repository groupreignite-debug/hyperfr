"""Export cover/cover.html to cover.png (1080x1920) with the pre-installed headless Chromium."""
import glob
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
chrome = (glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome") or ["chromium"])[0]
subprocess.run([chrome, "--headless=new", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=1",
                "--window-size=1080,1920", "--virtual-time-budget=4000",
                f"--screenshot={ROOT / 'cover.png'}", (ROOT / "cover" / "cover.html").as_uri()], check=True,
               capture_output=True)
print("wrote cover.png")
