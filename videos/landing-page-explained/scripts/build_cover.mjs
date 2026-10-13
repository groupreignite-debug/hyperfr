// Renders cover/cover.html → cover.png (1080×1920) with the preinstalled Chromium.
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
// playwright: local install, else the global one
const req = createRequire(import.meta.url);
let pw;
try { pw = req("playwright"); } catch { pw = req(execSync("npm root -g").toString().trim() + "/playwright"); }
const { chromium } = pw;
import { fileURLToPath } from "node:url";
import path from "node:path";
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto("file://" + path.join(root, "cover", "cover.html"));
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
await page.screenshot({ path: path.join(root, "cover.png") });
await browser.close();
console.log("wrote cover.png");
