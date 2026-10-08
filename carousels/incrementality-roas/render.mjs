// Renders slides/slide-1.html … slide-7.html to out/01.png … 07.png at 1080×1350.
// Usage: node render.mjs   (needs playwright; Chromium from PLAYWRIGHT_BROWSERS_PATH)
import { chromium } from "playwright";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, join } from "node:path";
import { mkdirSync } from "node:fs";

const root = dirname(fileURLToPath(import.meta.url));
const outDir = join(root, "out");
mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });

for (let n = 1; n <= 7; n++) {
  await page.goto(pathToFileURL(join(root, "slides", `slide-${n}.html`)).href, { waitUntil: "load" });
  await page.evaluate(async () => {
    // force every weight we use (Arabic + Latin subsets) to load, then wait for the font set
    await Promise.all([300, 400, 500, 700, 800, 900].map((w) => document.fonts.load(`${w} 40px Alexandria`, "صرفت ROAS")));
    await document.fonts.ready;
  });
  // fail loudly if Alexandria did not load (no fallback font in the export)
  const ok = await page.evaluate(() =>
    [300, 400, 500, 700, 800, 900].every(
      (w) => document.fonts.check(`${w} 40px Alexandria`, "صرفت") && document.fonts.check(`${w} 40px Alexandria`, "ROAS")
    )
  );
  const loaded = await page.evaluate(() => [...document.fonts].filter((f) => f.status === "loaded").length);
  if (!ok || loaded === 0) throw new Error(`slide ${n}: Alexandria not loaded`);
  const file = join(outDir, `${String(n).padStart(2, "0")}.png`);
  await page.screenshot({ path: file, omitBackground: false, clip: { x: 0, y: 0, width: 1080, height: 1350 } });
  console.log(`slide ${n} → ${file} (${loaded} font faces loaded)`);
}

await browser.close();
