import sys; sys.path.insert(0, __import__('os').path.dirname(__file__))
from frames_common import *
OUT = __import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'compositions', 'frames') + '/'
def W(cid, s): open(OUT + cid + '.html', 'w').write(s)
def mark(style, cut='#1a1a1a'):
    return f'<svg class="mk" viewBox="0 0 100 100" style="{style}">{GEN.format(cut=cut)}</svg>'

# ---------------- s06 scale ----------------
p='s06'
css = base_css(p, ['k800','p600','i700','i800']) + '''
    #s06-k { position: absolute; right: 90px; top: 380px; font-family: "IBM Plex Sans Arabic", sans-serif; font-weight: 600; font-size: 50px; color: rgba(245,241,234,0.6); direction: rtl; white-space: nowrap; }
    #s06-h { position: absolute; left: 60px; right: 90px; top: 470px; text-align: right; font-weight: 800; font-size: 92px; line-height: 1.4; }
    .mk { position: absolute; overflow: visible; }
    .s06-env { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }
    .s06-lab { position: absolute; left: 90px; right: 90px; top: 1340px; height: 40px; font-family: "Inter", sans-serif; font-weight: 800; font-size: 24px; letter-spacing: 0.2em; white-space: nowrap; }
    .s06-lab .n { position: absolute; left: 0; color: rgba(245,241,234,0.75); }
    .s06-lab .p { position: absolute; right: 0; color: #ff4d1a; }
    .s06-hair { position: absolute; border: 1.5px solid rgba(245,241,234,0.28); }
    .s06-bar { position: absolute; height: 14px; border-radius: 7px; background: rgba(245,241,234,0.16); }
    .s06-blk { position: absolute; background: rgba(245,241,234,0.07); border-radius: 10px; }'''
tiles = ''
for r in range(4):
    for c in range(3):
        x, y = 30 + c*120, 90 + r*130
        if (r, c) == (1, 1):
            tiles += f'<div id="s06-app" style="position: absolute; left: {x}px; top: {y}px; width: 96px; height: 96px; border-radius: 24px; background: #f5f1ea">{mark("left: 18px; top: 18px; width: 60px; height: 60px", "#f5f1ea")}</div>'
        else:
            tiles += f'<div class="s06-hair" style="left: {x}px; top: {y}px; width: 96px; height: 96px; border-radius: 24px"></div>'
html = f'''      <div class="s06-tag" id="s06-tag">SCALABLE<b>04</b></div>
      <div id="s06-k">الشعار البسيط…</div>
      <div id="s06-h" class="s06-ar">{words(p,'h','بيشتغل بكل مكان:',orange=(1,2))}</div>
      <div class="s06-env" id="s06-e1">
        <div class="s06-hair" style="left: 110px; top: 690px; width: 860px; height: 420px; background: rgba(245,241,234,0.04)"></div>
        <div style="position: absolute; left: 330px; top: 1110px; width: 6px; height: 150px; background: rgba(245,241,234,0.28)"></div>
        <div style="position: absolute; left: 744px; top: 1110px; width: 6px; height: 150px; background: rgba(245,241,234,0.28)"></div>
        {mark("left: 640px; top: 760px; width: 280px; height: 280px")}
        <div class="s06-bar" style="left: 170px; top: 830px; width: 380px; height: 34px; border-radius: 17px; background: rgba(245,241,234,0.22)"></div>
        <div class="s06-bar" style="left: 170px; top: 892px; width: 300px"></div>
        <div class="s06-bar" style="left: 170px; top: 926px; width: 240px"></div>
        <div class="s06-lab"><span class="n">BILLBOARD</span><span class="p">100%</span></div>
      </div>
      <div class="s06-env" id="s06-e2">
        <div class="s06-hair" style="left: 150px; top: 680px; width: 780px; height: 560px; border-radius: 18px; background: rgba(245,241,234,0.03)"></div>
        <div style="position: absolute; left: 150px; top: 740px; width: 780px; height: 1.5px; background: rgba(245,241,234,0.22)"></div>
        <div class="s06-hair" style="left: 176px; top: 702px; width: 16px; height: 16px; border-radius: 50%"></div>
        <div class="s06-hair" style="left: 202px; top: 702px; width: 16px; height: 16px; border-radius: 50%"></div>
        <div class="s06-hair" style="left: 228px; top: 702px; width: 16px; height: 16px; border-radius: 50%"></div>
        <div class="s06-bar" style="left: 380px; top: 703px; width: 320px; height: 16px"></div>
        {mark("left: 186px; top: 768px; width: 64px; height: 64px")}
        <div class="s06-bar" style="left: 560px; top: 793px; width: 80px"></div>
        <div class="s06-bar" style="left: 664px; top: 793px; width: 80px"></div>
        <div class="s06-bar" style="left: 768px; top: 793px; width: 120px; background: rgba(255,77,26,0.75)"></div>
        <div class="s06-blk" style="left: 186px; top: 870px; width: 708px; height: 200px"></div>
        <div class="s06-blk" style="left: 186px; top: 1090px; width: 222px; height: 120px"></div>
        <div class="s06-blk" style="left: 429px; top: 1090px; width: 222px; height: 120px"></div>
        <div class="s06-blk" style="left: 672px; top: 1090px; width: 222px; height: 120px"></div>
        <div class="s06-lab"><span class="n">WEBSITE</span><span class="p">25%</span></div>
      </div>
      <div class="s06-env" id="s06-e3">
        <div id="s06-phone" class="s06-hair" style="left: 330px; top: 640px; width: 420px; height: 660px; border-radius: 56px; background: rgba(245,241,234,0.03)">
          <div style="position: absolute; left: 160px; top: 26px; width: 100px; height: 22px; border-radius: 11px; background: rgba(245,241,234,0.14)"></div>
          {tiles}
        </div>
        <div class="s06-lab"><span class="n">APP ICON</span><span class="p">ON YOUR PHONE</span></div>
      </div>'''
js = '''      tl.fromTo("#s06-tag", { opacity: 0, x: 24 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, 0.05);
      tl.fromTo("#s06-k", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, V + 0.0);
      seq("#s06-h", [1.207, 1.707, 2.009]);
      // a big mark waits on the board before its word lands
      tl.fromTo("#s06-e1", { opacity: 0, scale: 1.08 }, { opacity: 0.35, scale: 1, duration: 0.6, ease: "expo.out" }, 0.1);
      tl.to("#s06-e1", { opacity: 1, duration: 0.3 }, V + 2.83);
      tl.fromTo("#s06-e1 .s06-lab", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, V + 2.9);
      tl.to("#s06-e1", { opacity: 0, scale: 0.9, duration: 0.25, ease: "power2.in" }, V + 3.43);
      tl.fromTo("#s06-e2", { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 0.45, ease: "expo.out" }, V + 3.66);
      tl.fromTo("#s06-e2 .s06-lab", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, V + 3.75);
      tl.to("#s06-e2", { opacity: 0, scale: 0.9, duration: 0.18, ease: "power2.in" }, V + 4.12);
      tl.fromTo("#s06-e3", { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 0.5, ease: "expo.out" }, V + 4.32);
      tl.fromTo("#s06-e3 .s06-lab", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, V + 4.45);
      tl.fromTo("#s06-app", { scale: 1.8 }, { scale: 1, duration: 0.7, ease: "back.out(1.6)" }, V + 5.0);
      tl.to("#s06-phone", { scale: 1.06, duration: 1.2, ease: "power2.out" }, V + 5.5);'''
W('s06-scale', frame('s06-scale', p, 6.9, css, html, js, 0.2))

# ---------------- s07 lesson ----------------
p='s07'
css = base_css(p, ['k800','k900','p600','i800']) + '''
    #s07-h { position: absolute; left: 60px; right: 60px; top: 360px; text-align: center; font-weight: 800; font-size: 88px; line-height: 1.4; }
    #s07-div { position: absolute; left: 539px; top: 560px; width: 2px; height: 640px; background: rgba(245,241,234,0.22); transform-origin: 50% 0%; }
    .s07-pan { position: absolute; top: 560px; width: 440px; height: 640px; }
    #s07-L { left: 90px; } #s07-R { left: 550px; }
    .s07-ttl { position: absolute; left: 0; right: 0; top: 10px; text-align: center; white-space: nowrap; }
    .s07-ttl .en { font-family: "Inter", sans-serif; font-weight: 800; font-size: 44px; letter-spacing: 0.06em; }
    .s07-ttl .ar { font-family: "Noto Kufi Arabic", sans-serif; font-weight: 800; font-size: 50px; margin-left: 14px; }
    .s07-vis { position: absolute; left: 50px; top: 140px; width: 340px; height: 340px; overflow: visible; }
    #s07-cap { position: absolute; left: 0; right: 0; top: 530px; text-align: center; direction: rtl; font-family: "IBM Plex Sans Arabic", sans-serif; font-weight: 600; font-size: 44px; color: rgba(245,241,234,0.62); white-space: nowrap; }
    #s07-end { position: absolute; left: 30px; right: 30px; top: 1250px; text-align: center; font-weight: 900; font-size: 116px; line-height: 1.35; }'''
html = f'''      <div id="s07-h" class="s07-ar">{words(p,'h','وهون الفرق:',orange=(1,))}</div>
      <div id="s07-div"></div>
      <div class="s07-pan" id="s07-L">
        <div class="s07-ttl" id="s07-Lt"><span class="en">LOGO</span><span class="ar">حلو</span></div>
        <svg class="s07-vis" id="s07-Lv" viewBox="-170 -170 340 340">
          <g fill="none" stroke="#f5f1ea" stroke-width="1.6" stroke-opacity="0.75">
            <circle r="160" /><circle r="146" stroke-dasharray="3 6" /><circle r="62" />
            <g stroke="#ffb000" stroke-opacity="0.85">
              <ellipse rx="26" ry="96" /><ellipse rx="26" ry="96" transform="rotate(30)" /><ellipse rx="26" ry="96" transform="rotate(60)" />
              <ellipse rx="26" ry="96" transform="rotate(90)" /><ellipse rx="26" ry="96" transform="rotate(120)" /><ellipse rx="26" ry="96" transform="rotate(150)" />
            </g>
            <path d="M-120 120 Q 0 60 120 120" /><path d="M-120 -120 Q 0 -60 120 -120" />
          </g>
          <g fill="#f5f1ea" fill-opacity="0.8">
            <circle cx="0" cy="-153" r="4" /><circle cx="0" cy="153" r="4" /><circle cx="-153" cy="0" r="4" /><circle cx="153" cy="0" r="4" />
            <rect x="-40" y="-8" width="80" height="16" rx="8" fill="#ff4d1a" fill-opacity="0.8" />
          </g>
        </svg>
        <div id="s07-cap">بيعجبك</div>
      </div>
      <div class="s07-pan" id="s07-R">
        <div class="s07-ttl" id="s07-Rt"><span class="en or">LOGO</span><span class="ar or">قوي</span></div>
        <svg class="s07-vis" id="s07-Rv" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="#ff4d1a" /><rect x="44" y="-4" width="12" height="62" fill="#1a1a1a" transform="rotate(38 50 50)" /><circle cx="50" cy="50" r="15" fill="#1a1a1a" /></svg>
      </div>
      <div id="s07-end" class="s07-ar">{words(p,'e','بيعلق بذاكرتك.',orange=(1,))}</div>'''
js = '''      seq("#s07-h", [0, 0.557]);
      tl.fromTo("#s07-div", { scaleY: 0 }, { scaleY: 1, duration: 0.8, ease: "expo.inOut" }, V + 0.3);
      tl.fromTo("#s07-Lt", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, V + 1.35);
      tl.fromTo("#s07-Lv", { opacity: 0, scale: 0.7, rotation: -20 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.8, ease: "expo.out" }, V + 1.37);
      tl.fromTo("#s07-cap", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, V + 2.37);
      // "بس اللوغو القوي…" — the strong side arrives and takes over
      tl.fromTo("#s07-Rt", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, V + 3.5);
      tl.fromTo("#s07-Rv", { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.55, ease: "back.out(1.7)" }, V + 3.6);
      tl.to("#s07-L", { opacity: 0.18, scale: 0.72, x: -40, duration: 0.9, ease: "expo.inOut" }, V + 4.25);
      tl.to("#s07-div", { x: -250, opacity: 0.35, duration: 0.9, ease: "expo.inOut" }, V + 4.25);
      tl.to("#s07-R", { x: -170, scale: 1.3, duration: 0.9, ease: "expo.inOut" }, V + 4.25);
      // "بيعلق بذاكرتك."
      word("#s07-e1", V + 4.84);
      tl.fromTo("#s07-e2", { opacity: 0, y: 50, scale: 0.88 }, { opacity: 1, y: 0, scale: 1, duration: 0.65, ease: "back.out(1.6)" }, V + 5.25);
      tl.to("#s07-h", { opacity: 0.3, duration: 0.4 }, V + 4.8);'''
W('s07-lesson', frame('s07-lesson', p, 6.7, css, html, js, 0.2))

# ---------------- s08 try it ----------------
p='s08'
css = base_css(p, ['k800','k900','p600','i700','i800']) + '''
    #s08-h { position: absolute; left: 60px; right: 90px; top: 372px; text-align: right; font-weight: 900; font-size: 104px; line-height: 1.4; }
    #s08-k { position: absolute; right: 90px; top: 525px; font-family: "IBM Plex Sans Arabic", sans-serif; font-weight: 600; font-size: 52px; color: rgba(245,241,234,0.68); direction: rtl; white-space: nowrap; }
    #s08-box { position: absolute; left: 330px; top: 680px; width: 420px; height: 420px; border: 3px dashed rgba(245,241,234,0.45); border-radius: 28px; }
    #s08-box .t { position: absolute; left: 0; right: 0; top: 100px; text-align: center; font-family: "Noto Kufi Arabic", sans-serif; font-weight: 800; font-size: 76px; color: rgba(245,241,234,0.75); direction: rtl; }
    #s08-box .e { position: absolute; left: 0; right: 0; top: 300px; text-align: center; font-family: "Inter", sans-serif; font-weight: 700; font-size: 20px; letter-spacing: 0.24em; color: rgba(245,241,234,0.4); }
    #s08-px { position: absolute; left: 330px; right: 330px; top: 1130px; height: 40px; font-family: "Inter", sans-serif; font-weight: 800; font-size: 24px; letter-spacing: 0.2em; white-space: nowrap; }
    #s08-px1 { position: absolute; left: 0; right: 0; text-align: center; color: rgba(245,241,234,0.6); }
    #s08-px2 { position: absolute; left: 0; right: 0; text-align: center; color: #ff4d1a; }
    #s08-end { position: absolute; left: 40px; right: 40px; top: 1300px; text-align: center; font-weight: 900; font-size: 116px; line-height: 1.35; }'''
html = f'''      <div class="s08-tag" id="s08-tag">TRY IT<b>05</b></div>
      <div id="s08-h" class="s08-ar">{words(p,'h','جرّب هلّق:',orange=(1,))}</div>
      <div id="s08-k">صغّر شعارك لقدّ أيقونة.</div>
      <div id="s08-box"><div class="t">شعارك</div><div class="e">YOUR LOGO</div></div>
      <div id="s08-px"><span id="s08-px1">420 PX</span><span id="s08-px2">48 PX</span></div>
      <div id="s08-end" class="s08-ar">{words(p,'e','بعدك بتعرفو؟',orange=(1,))}</div>'''
js = '''      tl.fromTo("#s08-tag", { opacity: 0, x: 24 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, 0.05);
      word("#s08-h1", V + 0);
      pop("#s08-h2", V + 0.453);
      tl.fromTo("#s08-box", { opacity: 0, scale: 1.1 }, { opacity: 1, scale: 1, duration: 0.6, ease: "expo.out" }, 0.1);
      tl.fromTo("#s08-px1", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.4);
      // "صغّر شعارك لقدّ أيقونة."
      tl.fromTo("#s08-k", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, V + 1.16);
      tl.to("#s08-box", { scale: 0.115, borderRadius: "120px", duration: 1.0, ease: "expo.inOut" }, V + 1.6);
      tl.to("#s08-px1", { opacity: 0, duration: 0.2 }, V + 2.1);
      tl.fromTo("#s08-px2", { opacity: 0 }, { opacity: 1, duration: 0.25 }, V + 2.25);
      // "بعدك بتعرفو؟"
      word("#s08-e1", V + 2.926);
      tl.fromTo("#s08-e2", { opacity: 0, y: 50, scale: 0.86 }, { opacity: 1, y: 0, scale: 1, duration: 0.65, ease: "back.out(1.7)" }, V + 3.26);'''
W('s08-try', frame('s08-try', p, 4.8, css, html, js, 0.3))

# ---------------- s09 comment ----------------
p='s09'
css = base_css(p, ['k800','p600','i700']) + '''
    #s09-h { position: absolute; left: 40px; right: 40px; top: 400px; text-align: center; font-weight: 800; font-size: 92px; line-height: 1.4; }
    #s09-card { position: absolute; left: 110px; top: 690px; width: 860px; height: 300px; border: 1.5px solid rgba(245,241,234,0.22); border-radius: 30px; background: rgba(245,241,234,0.04); }
    #s09-av { position: absolute; right: 40px; top: 48px; width: 76px; height: 76px; border-radius: 50%; border: 3px solid #ff4d1a; }
    #s09-n1 { position: absolute; right: 140px; top: 58px; width: 220px; height: 18px; border-radius: 9px; background: rgba(245,241,234,0.3); }
    #s09-n2 { position: absolute; right: 140px; top: 94px; width: 140px; height: 14px; border-radius: 7px; background: rgba(245,241,234,0.14); }
    #s09-in { position: absolute; left: 40px; right: 40px; top: 170px; height: 86px; border-radius: 43px; border: 1.5px solid rgba(245,241,234,0.3); }
    #s09-ph { position: absolute; right: 36px; top: 0; line-height: 84px; direction: rtl; font-family: "IBM Plex Sans Arabic", sans-serif; font-weight: 600; font-size: 38px; color: rgba(245,241,234,0.45); white-space: nowrap; }
    #s09-caret { position: absolute; right: 30px; top: 22px; width: 3px; height: 42px; background: #ff4d1a; }
    #s09-send { position: absolute; left: 12px; top: 10px; width: 64px; height: 64px; border-radius: 50%; background: #ff4d1a; }
    #s09-send svg { position: absolute; left: 16px; top: 16px; width: 32px; height: 32px; }
    #s09-opts { position: absolute; left: 110px; right: 110px; top: 1090px; height: 140px; }
    .s09-o { position: absolute; top: 0; width: 400px; height: 130px; border-radius: 65px; text-align: center; direction: rtl; font-family: "Noto Kufi Arabic", sans-serif; font-weight: 800; font-size: 60px; line-height: 126px; white-space: nowrap; }
    #s09-o1 { right: 0; background: #ff4d1a; color: #1a1a1a; }
    #s09-o2 { left: 0; border: 3px solid rgba(245,241,234,0.4); color: #f5f1ea; }
    .s09-o b { font-family: "Inter", sans-serif; font-weight: 700; margin-left: 18px; }'''
html = f'''      <div id="s09-h" class="s09-ar">{words(p,'h','اكتبلنا بالكومنتات:',orange=(1,))}</div>
      <div id="s09-card">
        <div id="s09-av"></div><div id="s09-n1"></div><div id="s09-n2"></div>
        <div id="s09-in"><span id="s09-ph">اكتب تعليقك…</span><i id="s09-caret"></i>
          <div id="s09-send"><svg viewBox="0 0 32 32"><path d="M4 16 L28 4 L20 28 L16 18 Z" fill="#1a1a1a" /></svg></div>
        </div>
      </div>
      <div id="s09-opts">
        <div class="s09-o" id="s09-o1"><b>✓</b>نجح</div>
        <div class="s09-o" id="s09-o2"><b>✕</b>لأ</div>
      </div>'''
js = '''      word("#s09-h1", V + 0); pop("#s09-h2", V + 0.534);
      tl.fromTo("#s09-card", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.6, ease: "expo.out" }, V + 0.6);
      [1.2, 1.7, 2.2, 2.7, 3.2].forEach((t) => {
        tl.set("#s09-caret", { opacity: 0 }, V + t);
        tl.set("#s09-caret", { opacity: 1 }, V + t + 0.25);
      });
      // "نجح ولا لأ؟"
      pop("#s09-o1", V + 2.1);
      pop("#s09-o2", V + 2.79);'''
W('s09-comment', frame('s09-comment', p, 4.0, css, html, js, 0.2))

# ---------------- s10 statement ----------------
p='s10'
css = '\n    '.join([FONTS['k800'], FONTS['k900']]) + '''
    #root { position: absolute; inset: 0; color: #f5f1ea; font-family: "Noto Kufi Arabic", sans-serif; }
    #s10-stage { position: absolute; inset: 0; background: #1a1a1a; }
    .s10-ar { font-family: "Noto Kufi Arabic", sans-serif; direction: rtl; white-space: nowrap; text-align: center; }
    .s10-w { display: inline-block; }
    .or { color: #ff4d1a; }
    #s10-l1 { position: absolute; left: 40px; right: 40px; top: 600px; font-weight: 800; font-size: 62px; line-height: 1.4; }
    #s10-l2 { position: absolute; left: 30px; right: 30px; top: 780px; font-weight: 900; line-height: 1.5; }
    #s10-l2 .row { display: block; }
    #s10-r1 { font-size: 100px; } #s10-r2 { font-size: 124px; } #s10-r3 { font-size: 168px; }
    #s10-e5 { position: relative; }
    #s10-ul { position: absolute; left: 4%; right: 4%; bottom: 18px; height: 16px; background: #ff4d1a; transform-origin: 100% 50%; }'''
html = f'''      <div id="s10-l1" class="s10-ar">{words(p,'a','البساطة مش نقص بالتفاصيل.')}</div>
      <div id="s10-l2" class="s10-ar" data-layout-allow-overlap>
        <span class="row" id="s10-r1">{words(p,'e','البساطة إنك تختار',orange=(2,))}</span>
        <span class="row or" id="s10-r2"><span data-layout-allow-overlap class="s10-w" id="s10-e4">التفاصيل</span></span>
        <span class="row or" id="s10-r3"><span data-layout-allow-overlap class="s10-w" id="s10-e5">الصح.<i id="s10-ul"></i></span></span>
      </div>'''
js = '''      seq("#s10-a", [0, 0.731, 0.94, 1.196]);
      tl.to("#s10-l1", { opacity: 0.35, y: -40, duration: 0.7, ease: "expo.out" }, V + 2.0);
      seq("#s10-e", [2.148, 2.798, 3.158, 3.599]);
      tl.fromTo("#s10-e5", { opacity: 0, y: 60, scale: 0.86 }, { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "back.out(1.6)" }, V + 4.226);
      tl.fromTo("#s10-ul", { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "expo.inOut" }, V + 4.65);'''
s = frame('s10-statement', p, 6.0, css, html, js, 0.3)
W('s10-statement', s)

# ---------------- s11 end card ----------------
W('s11-endcard', '''<template>
  <style>
    @font-face { font-family: "Inter"; font-weight: 600; src: url("assets/fonts/inter-latin-600-normal.woff2") format("woff2"); }
    #root { position: absolute; inset: 0; color: #f5f1ea; font-family: "Inter", sans-serif; }
    #s11-bg { position: absolute; inset: 0; background: #1a1a1a; }
    /* the supplied logo, untouched: framed only; its black field blends into the charcoal */
    #s11-logo { position: absolute; left: 160px; top: 720px; width: 760px; }
    #s11-img { display: block; width: 760px; height: auto; mix-blend-mode: lighten; }
    #s11-svc { position: absolute; left: 60px; right: 60px; top: 1215px; text-align: center; font-weight: 600; font-size: 25px; letter-spacing: 0.26em; color: rgba(245,241,234,0.62); white-space: nowrap; }
    #s11-svc i { font-style: normal; color: #ff4d1a; margin: 0 14px; }
  </style>

  <div id="root" data-composition-id="s11-endcard" data-width="1080" data-height="1920">
    <div id="s11-bg" class="clip" data-start="0" data-duration="4" data-track-index="0">
      <div id="s11-logo"><img id="s11-img" src="assets/reignite/reignite-group-logo.png" alt="Reignite Group" /></div>
      <div id="s11-svc">BRANDING<i>•</i>DIGITAL MARKETING<i>•</i>DESIGN</div>
    </div>
  </div>

  <script>
    (function () {
      const tl = gsap.timeline({ paused: true });
      // minimal: fade + 98% → 100%, then a quiet fade out (final frame)
      tl.fromTo("#s11-img", { opacity: 0, scale: 0.98 }, { opacity: 1, scale: 1, duration: 1.4, ease: "power2.out" }, 0.1);
      tl.fromTo("#s11-svc", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 0.8);
      tl.to(["#s11-img", "#s11-svc"], { opacity: 0, duration: 0.6, ease: "power2.in" }, 3.35);
      window.__timelines["s11-endcard"] = tl;
    })();
  </script>
</template>
''')
print('b ok')
