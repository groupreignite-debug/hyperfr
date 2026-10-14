# shared snippets for v2 frame files
NIKE = 'M24 7.8L6.442 15.276c-1.456.616-2.679.925-3.668.925-1.12 0-1.933-.392-2.437-1.177-.317-.504-.41-1.143-.28-1.918.13-.775.476-1.6 1.036-2.478.467-.71 1.232-1.643 2.297-2.8a6.122 6.122 0 00-.784 1.848c-.28 1.195-.028 2.072.756 2.632.373.261.886.392 1.54.392.522 0 1.11-.084 1.764-.252L24 7.8z'
APPLE = 'M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701'
MCD = 'M17.243 3.006c2.066 0 3.742 8.714 3.742 19.478H24c0-11.588-3.042-20.968-6.766-20.968-2.127 0-4.007 2.81-5.248 7.227-1.241-4.416-3.121-7.227-5.231-7.227C3.031 1.516 0 10.888 0 22.476h3.014c0-10.763 1.658-19.47 3.724-19.47 2.066 0 3.741 8.05 3.741 17.98h2.997c0-9.93 1.684-17.98 3.75-17.98Z'
GEN = '<circle cx="50" cy="50" r="50" fill="#ff4d1a" /><rect x="44" y="-4" width="12" height="62" fill="{cut}" transform="rotate(38 50 50)" /><circle cx="50" cy="50" r="15" fill="{cut}" />'
FONTS = {
 'k800': '@font-face { font-family: "Noto Kufi Arabic"; font-weight: 800; src: url("assets/fonts/noto-kufi-arabic-arabic-800-normal.woff2") format("woff2"); }',
 'k900': '@font-face { font-family: "Noto Kufi Arabic"; font-weight: 900; src: url("assets/fonts/noto-kufi-arabic-arabic-900-normal.woff2") format("woff2"); }',
 'p600': '@font-face { font-family: "IBM Plex Sans Arabic"; font-weight: 600; src: url("assets/fonts/ibm-plex-sans-arabic-arabic-600-normal.woff2") format("woff2"); }',
 'i600': '@font-face { font-family: "Inter"; font-weight: 600; src: url("assets/fonts/inter-latin-600-normal.woff2") format("woff2"); }',
 'i700': '@font-face { font-family: "Inter"; font-weight: 700; src: url("assets/fonts/inter-latin-700-normal.woff2") format("woff2"); }',
 'i800': '@font-face { font-family: "Inter"; font-weight: 800; src: url("assets/fonts/inter-latin-800-normal.woff2") format("woff2"); }',
}
def base_css(p, fonts):
    f = "\n    ".join(FONTS[k] for k in dict.fromkeys(list(fonts) + ['p600']))
    return f'''{f}
    #root {{ position: absolute; inset: 0; color: #f5f1ea; font-family: "IBM Plex Sans Arabic", sans-serif; }}
    #{p}-stage {{ position: absolute; inset: 0; }}
    .{p}-ar {{ font-family: "Noto Kufi Arabic", sans-serif; direction: rtl; white-space: nowrap; }}
    .{p}-w {{ display: inline-block; }}
    .or {{ color: #ff4d1a; }}
    .{p}-tag {{ position: absolute; right: 90px; top: 318px; font-family: "Inter", sans-serif; font-weight: 700; font-size: 22px; letter-spacing: 0.24em; color: rgba(245,241,234,0.6); white-space: nowrap; }}
    .{p}-tag b {{ color: #ff4d1a; font-weight: 800; margin-left: 14px; }}'''
def words(p, pre, text, orange=()):
    out=[]
    for i,w in enumerate(text.split(' ')):
        cls = f'{p}-w or' if i in orange else f'{p}-w'
        out.append(f'<span data-layout-allow-overlap class="{cls}" id="{p}-{pre}{i+1}">{w}</span>')
    return ' '.join(out)
JS_HEAD = '''const tl = gsap.timeline({ paused: true });
      const word = (sel, t) => tl.fromTo(sel, { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, t);
      const pop = (sel, t) => tl.fromTo(sel, { opacity: 0, y: 40, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "back.out(1.8)" }, t);
      const seq = (pre, times) => times.forEach((t, i) => word(pre + (i + 1), V + t));'''
def frame(cid, p, dur, css, html, js, V):
    return f'''<template>
  <style>
    {css}
  </style>

  <div id="root" data-composition-id="{cid}" data-width="1080" data-height="1920">
    <div id="{p}-stage" class="clip" data-start="0" data-duration="{dur}" data-track-index="0">
{html}
    </div>
  </div>

  <script>
    (function () {{
      const V = {V};
      {JS_HEAD}
{js}
      window.__timelines["{cid}"] = tl;
    }})();
  </script>
</template>
'''
