import sys; sys.path.insert(0, __import__('os').path.dirname(__file__))
from frames_common import *
OUT = __import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'compositions', 'frames') + '/'
def W(cid, s): open(OUT + cid + '.html', 'w').write(s)

# ---------------- s01 cold open ----------------
p='s01'
css = base_css(p, ['k800','k900','p600','i700','i800']) + '''
    #s01-row { position: absolute; left: 90px; top: 560px; width: 900px; height: 300px; }
    .s01-card { position: absolute; top: 0; width: 280px; height: 280px; border: 1.5px solid rgba(245,241,234,0.16); background: rgba(245,241,234,0.025); }
    .s01-card .s01-tk { position: absolute; width: 18px; height: 18px; border-color: #ff4d1a; border-style: solid; border-width: 0; }
    .s01-tk.a { left: -2px; top: -2px; border-left-width: 3px; border-top-width: 3px; }
    .s01-tk.b { right: -2px; bottom: -2px; border-right-width: 3px; border-bottom-width: 3px; }
    .s01-card svg.m { position: absolute; left: 50%; top: 50%; margin-left: -90px; margin-top: -90px; width: 180px; height: 180px; overflow: visible; }
    .s01-ok { position: absolute; right: -18px; top: -18px; width: 52px; height: 52px; border-radius: 50%; background: #ff4d1a; }
    .s01-ok svg { position: absolute; left: 11px; top: 12px; width: 30px; height: 28px; }
    .s01-q { position: absolute; left: 0; right: 0; top: 300px; text-align: center; font-family: "Inter", sans-serif; font-weight: 800; font-size: 34px; color: rgba(245,241,234,0.35); letter-spacing: 0.3em; }
    #s01-a { position: absolute; left: 40px; right: 40px; top: 960px; text-align: center; font-weight: 900; line-height: 1.45; }
    #s01-a .l1 { display: block; font-size: 120px; }
    #s01-a .l2 { display: block; font-size: 90px; }
    #s01-b { position: absolute; left: 40px; right: 40px; top: 1000px; text-align: center; }
    #s01-bin { position: relative; display: inline-block; font-family: "IBM Plex Sans Arabic", sans-serif; font-weight: 600; font-size: 56px; color: rgba(245,241,234,0.65); direction: rtl; white-space: nowrap; }
    #s01-bx { position: absolute; left: -12px; right: -12px; top: 54%; height: 5px; background: #ff4d1a; transform-origin: 100% 50%; }
    #s01-c { position: absolute; left: 40px; right: 40px; top: 1120px; text-align: center; font-weight: 900; font-size: 80px; line-height: 1.4; }'''
OK = '<svg viewBox="0 0 32 30"><path d="M3 16 L12 25 L29 5" fill="none" stroke="#1a1a1a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" /></svg>'
cards = ''
for i,(left,path,fill) in enumerate([(620,NIKE,'#f5f1ea'),(310,APPLE,'#f5f1ea'),(0,MCD,'#ffb000')]):
    cards += f'''        <div class="s01-card" id="s01-c{i+1}" style="left: {left}px">
          <i class="s01-tk a"></i><i class="s01-tk b"></i>
          <svg class="m" viewBox="0 0 24 24"><path fill="{fill}" d="{path}"/></svg>
          <div class="s01-ok" id="s01-k{i+1}">{OK}</div>
          <div class="s01-q">? ? ?</div>
        </div>
'''
html = f'''      <div id="s01-row">
{cards}      </div>
      <div id="s01-a" class="s01-ar"><span class="l1">{words(p,'a','ولا اسم…')}</span><span class="l2">{words(p,'b','وعرفتهن التلاتة.',orange=(1,))}</span></div>
      <div id="s01-b"><span id="s01-bin">السبب مش إنّو الشركات كبيرة.<i id="s01-bx"></i></span></div>
      <div id="s01-c" class="s01-ar">{words(p,'d','السبب إنّو الشعار بسيط.',orange=(3,))}</div>'''
js = '''      // cold open: three marks, no names, snap in before a word is said
      [["#s01-c1", 0.05], ["#s01-c2", 0.3], ["#s01-c3", 0.55]].forEach(([c, t]) => {
        tl.fromTo(c, { opacity: 0, scale: 0.6, y: 50 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.7)" }, t);
        tl.fromTo(c + " svg.m", { scale: 0.3 }, { scale: 1, duration: 0.5, ease: "expo.out" }, t + 0.05);
        tl.fromTo(c + " .s01-q", { opacity: 0 }, { opacity: 1, duration: 0.3 }, t + 0.2);
      });
      // VO1 at 1.1 — "ولا اسم… وعرفتهن التلاتة."
      const A = 1.1;
      tl.fromTo("#s01-a1", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, A + 0.0);
      tl.fromTo("#s01-a2", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, A + 0.27);
      tl.fromTo("#s01-b1", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, A + 0.94);
      pop("#s01-b2", A + 1.49);
      ["#s01-k1", "#s01-k2", "#s01-k3"].forEach((k, i) => {
        tl.fromTo(k, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(2.4)" }, A + 1.5 + i * 0.12);
      });
      tl.to(".s01-q", { opacity: 0, duration: 0.3 }, A + 1.5);
      // VO2 at 3.6 — not the company size… the simple mark
      const B = 3.6;
      tl.to("#s01-a", { opacity: 0, y: -30, duration: 0.4, ease: "power2.in" }, B - 0.15);
      tl.fromTo("#s01-bin", { opacity: 0, y: 26 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, B + 0.0);
      tl.fromTo("#s01-row", { scale: 1 }, { scale: 1.05, duration: 1.6, ease: "power2.out" }, B + 1.1);
      tl.fromTo("#s01-bx", { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: "power3.inOut" }, B + 2.55);
      tl.to("#s01-bin", { opacity: 0.3, duration: 0.4 }, B + 2.9);
      tl.to("#s01-row", { scale: 0.92, duration: 0.8, ease: "expo.out" }, B + 3.0);
      word("#s01-d1", B + 3.07); word("#s01-d2", B + 3.48); word("#s01-d3", B + 3.74);
      pop("#s01-d4", B + 4.13);'''
W('s01-cold', frame('s01-cold', p, 8.6, css, html, js, 0))

# ---------------- s02 setup ----------------
p='s02'
css = base_css(p, ['k800','p600','i700']) + '''
    #s02-h1 { position: absolute; left: 60px; right: 60px; top: 370px; text-align: center; font-weight: 800; font-size: 66px; line-height: 1.4; }
    #s02-h2 { position: absolute; left: 60px; right: 60px; top: 490px; text-align: center; }
    #s02-h2in { position: relative; display: inline-block; font-family: "IBM Plex Sans Arabic", sans-serif; font-weight: 600; font-size: 56px; color: rgba(245,241,234,0.62); direction: rtl; white-space: nowrap; }
    #s02-h2x { position: absolute; left: -10px; right: -10px; top: 54%; height: 5px; background: #ff4d1a; transform-origin: 100% 50%; }
    #s02-emb { position: absolute; left: 270px; top: 680px; width: 540px; height: 540px; overflow: visible; }
    .s02-lab { position: absolute; top: 1252px; font-family: "Inter", sans-serif; font-weight: 700; font-size: 24px; letter-spacing: 0.24em; white-space: nowrap; }
    #s02-add { left: 90px; color: rgba(245,241,234,0.55); }
    #s02-sub { right: 90px; color: #ff4d1a; }
    #s02-fin { position: absolute; left: 40px; right: 40px; top: 1320px; text-align: center; }
    #s02-finin { position: relative; display: inline-block; font-weight: 800; font-size: 96px; line-height: 1.35; }
    #s02-ful { position: absolute; left: 0; right: 0; bottom: -6px; height: 14px; background: #ff4d1a; transform-origin: 100% 50%; }'''
html = f'''      <div id="s02-h1" class="s02-ar">{words(p,'a','أصعب شي بتصميم الشعار',orange=(3,))}</div>
      <div id="s02-h2"><span id="s02-h2in">مش إنك تزيد تفاصيل…<i id="s02-h2x"></i></span></div>
      <svg id="s02-emb" viewBox="-270 -270 540 540">
        <g fill="none" stroke="#f5f1ea" stroke-width="3">
          <circle id="s02-e1" r="258" />
          <circle id="s02-e2" r="232" stroke-dasharray="6 10" stroke-opacity="0.7" />
          <circle id="s02-e3" r="176" stroke-opacity="0.85" />
          <g id="s02-e4" stroke-opacity="0.8">
            <line x1="0" y1="-258" x2="0" y2="-206" /><line x1="0" y1="258" x2="0" y2="206" />
            <line x1="-258" y1="0" x2="-206" y2="0" /><line x1="258" y1="0" x2="206" y2="0" />
            <line x1="182" y1="-182" x2="146" y2="-146" /><line x1="-182" y1="-182" x2="-146" y2="-146" />
            <line x1="182" y1="182" x2="146" y2="146" /><line x1="-182" y1="182" x2="-146" y2="146" />
          </g>
          <path id="s02-e5" d="M-176 0 L0 -176 L176 0 L0 176 Z" stroke-opacity="0.6" />
          <line id="s02-e6" x1="-176" y1="-176" x2="176" y2="176" stroke-opacity="0.45" />
          <line id="s02-e7" x1="176" y1="-176" x2="-176" y2="176" stroke-opacity="0.45" />
        </g>
        <g fill="#f5f1ea">
          <path id="s02-e8" d="M0 -246 l9 -14 l9 14 l-9 14 z M0 246 l9 -14 l9 14 l-9 14 z" transform="translate(-9 0)" />
          <rect id="s02-e9" x="-150" y="96" width="300" height="46" rx="4" fill-opacity="0.9" />
          <g id="s02-e10" fill-opacity="0.75"><rect x="-110" y="-128" width="220" height="12" rx="6" /><rect x="-70" y="-104" width="140" height="10" rx="5" /></g>
          <g id="s02-e11"><circle cx="-226" cy="-60" r="7" /><circle cx="226" cy="-60" r="7" /><circle cx="-226" cy="60" r="7" /><circle cx="226" cy="60" r="7" /></g>
        </g>
        <rect id="s02-e12" x="-120" y="104" width="240" height="30" fill="#1a1a1a" fill-opacity="0.9" />
        <circle id="s02-core" r="74" fill="#ff4d1a" />
      </svg>
      <div class="s02-lab" id="s02-add">+ ADD DETAIL</div>
      <div class="s02-lab" id="s02-sub">− REMOVE</div>
      <div id="s02-fin" class="s02-ar"><span id="s02-finin">{words(p,'f','إنك تعرف شو تشيل.',orange=(3,))}<i id="s02-ful"></i></span></div>'''
js = '''      seq("#s02-a", [0, 0.395, 0.511, 1.033]);
      tl.fromTo("#s02-core", { scale: 0, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.6, ease: "back.out(1.7)" }, 0.05);
      tl.fromTo("#s02-e3", { scale: 0.6, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.6, ease: "expo.out" }, 0.2);
      tl.fromTo("#s02-e1", { scale: 0.6, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.7, ease: "expo.out" }, 0.35);
      // "مش إنك تزيد تفاصيل…" — details pile on
      tl.fromTo("#s02-h2in", { opacity: 0, y: 26 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, V + 1.46);
      tl.fromTo("#s02-add", { opacity: 0, x: -20 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, V + 1.5);
      const extras = ["#s02-e2", "#s02-e4", "#s02-e5", "#s02-e6", "#s02-e7", "#s02-e8", "#s02-e9", "#s02-e12", "#s02-e10", "#s02-e11"];
      extras.forEach((e, i) => {
        tl.fromTo(e, { opacity: 0, scale: 1.25, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1, duration: 0.3, ease: "power3.out" }, V + 1.55 + i * 0.1);
      });
      // "هوّي إنك تعرف شو تشيل." — subtract to one shape
      tl.fromTo("#s02-h2x", { scaleX: 0 }, { scaleX: 1, duration: 0.35, ease: "power3.inOut" }, V + 2.85);
      tl.to("#s02-h2in", { opacity: 0.3, duration: 0.35 }, V + 3.1);
      tl.to("#s02-add", { opacity: 0.2, duration: 0.3 }, V + 2.9);
      tl.fromTo("#s02-sub", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, V + 3.2);
      extras.slice().reverse().concat(["#s02-e1", "#s02-e3"]).forEach((e, i) => {
        tl.to(e, { opacity: 0, scale: 0.85, duration: 0.24, ease: "power2.in" }, V + 3.25 + i * 0.07);
      });
      seq("#s02-f", [3.518, 3.796, 4.11]);
      pop("#s02-f4", V + 4.27);
      tl.to("#s02-core", { scale: 1.9, duration: 0.8, ease: "expo.out" }, V + 4.1);
      tl.fromTo("#s02-ful", { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "expo.inOut" }, V + 4.55);'''
W('s02-setup', frame('s02-setup', p, 5.4, css, html, js, 0.2))

# ---------------- s03 nike ----------------
p='s03'
css = base_css(p, ['k800','i700','i800']) + '''
    #s03-h { position: absolute; left: 60px; right: 90px; top: 372px; text-align: right; font-weight: 800; font-size: 96px; line-height: 1.4; }
    #s03-art { position: absolute; left: 110px; top: 650px; width: 860px; height: 336px; }
    #s03-box { position: absolute; inset: 0; overflow: visible; }
    #s03-sw { position: absolute; left: 0; top: 0; width: 860px; height: 336px; overflow: visible; }
    #s03-meter { position: absolute; left: 110px; top: 1080px; width: 860px; height: 60px; }
    #s03-bar { position: absolute; left: 0; top: 0; width: 860px; height: 6px; background: rgba(245,241,234,0.14); }
    #s03-fill { position: absolute; left: 0; top: 0; width: 860px; height: 6px; background: #ff4d1a; transform-origin: 0% 50%; }
    #s03-sec { position: absolute; left: 0; top: 24px; font-family: "Inter", sans-serif; font-weight: 800; font-size: 24px; letter-spacing: 0.2em; color: #ff4d1a; }
    #s03-one { position: absolute; right: 0; top: 24px; font-family: "Inter", sans-serif; font-weight: 800; font-size: 24px; letter-spacing: 0.2em; color: rgba(245,241,234,0.6); }
    #s03-end { position: absolute; left: 40px; right: 40px; top: 1260px; text-align: center; font-weight: 800; font-size: 110px; line-height: 1.4; }
    #s03-ok { display: inline-block; width: 92px; height: 92px; border-radius: 50%; background: #ff4d1a; vertical-align: 6px; margin-right: 26px; position: relative; }
    #s03-ok svg { position: absolute; left: 21px; top: 23px; width: 50px; height: 46px; }'''
html = f'''      <div class="s03-tag" id="s03-tag">SIMPLICITY<b>01</b></div>
      <div id="s03-h" class="s03-ar">{words(p,'h','نايك: شكل واحد.',orange=(0,))}</div>
      <div id="s03-art">
        <svg id="s03-box" viewBox="0 0 860 336">
          <g fill="none" stroke="#f5f1ea" stroke-opacity="0.28" stroke-width="1.5">
            <rect id="s03-bb" x="1" y="1" width="858" height="334" stroke-dasharray="2386" stroke-dashoffset="2386" />
          </g>
          <line id="s03-tan" x1="96" y1="300" x2="860" y2="12" stroke="#ff4d1a" stroke-width="2" stroke-dasharray="817" stroke-dashoffset="817" />
        </svg>
        <svg id="s03-sw" viewBox="0 7.4 24 9.2"><path fill="#f5f1ea" d="{NIKE}"/></svg>
      </div>
      <div id="s03-meter"><div id="s03-bar"></div><div id="s03-fill"></div><div id="s03-sec">1 SEC</div><div id="s03-one">1 SHAPE</div></div>
      <div id="s03-end" class="s03-ar"><span data-layout-allow-overlap class="s03-w or" id="s03-e1">وبتعرفو.</span><span id="s03-ok">{OK.replace('stroke-width="5"','stroke-width="4.5"')}</span></div>'''
js = '''      tl.fromTo("#s03-tag", { opacity: 0, x: 24 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, 0.05);
      seq("#s03-h", [0, 0.708, 1.033]);
      tl.to("#s03-bb", { strokeDashoffset: 0, duration: 0.8, ease: "power2.inOut" }, 0.05);
      tl.fromTo("#s03-sw", { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.8, ease: "expo.inOut" }, 0.15);
      tl.to("#s03-tan", { strokeDashoffset: 0, duration: 0.6, ease: "power3.inOut" }, V + 0.7);
      tl.fromTo("#s03-one", { opacity: 0 }, { opacity: 1, duration: 0.3 }, V + 0.75);
      // "بتشوفو لثانية…" — a one-second glance
      tl.fromTo("#s03-meter", { opacity: 0 }, { opacity: 1, duration: 0.25 }, V + 1.45);
      tl.fromTo("#s03-fill", { scaleX: 0 }, { scaleX: 1, duration: 0.9, ease: "none" }, V + 1.59);
      tl.to(["#s03-box"], { opacity: 0, duration: 0.3 }, V + 1.55);
      tl.set("#s03-sw", { opacity: 0 }, V + 1.6);
      tl.set("#s03-sw", { opacity: 1 }, V + 1.82);
      tl.set("#s03-sw", { opacity: 0 }, V + 2.1);
      // "وبتعرفو."
      tl.set("#s03-sw", { opacity: 1 }, V + 2.42);
      pop("#s03-e1", V + 2.46);
      tl.fromTo("#s03-ok", { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }, V + 2.7);'''
W('s03-nike', frame('s03-nike', p, 3.8, css, html, js, 0.2).replace('{OK}', OK))

# ---------------- s04 apple ----------------
p='s04'
css = base_css(p, ['k800','i600','i700','i800']) + '''
    #s04-h { position: absolute; left: 60px; right: 90px; top: 372px; text-align: right; font-weight: 800; font-size: 90px; line-height: 1.4; }
    #s04-art, #s04-geo { position: absolute; left: 310px; top: 600px; width: 460px; height: 460px; overflow: visible; }
    #s04-word { position: absolute; left: 0; right: 0; top: 1090px; text-align: center; }
    #s04-wordin { clip-path: inset(-20% 0% -20% 0%); position: relative; display: inline-block; font-family: "Inter", sans-serif; font-weight: 600; font-size: 66px; color: #f5f1ea; }
    #s04-wx { position: absolute; left: -16px; right: -16px; top: 52%; height: 5px; background: #ff4d1a; transform-origin: 0% 50%; }
    #s04-lA { position: absolute; left: 60px; right: 60px; top: 1230px; text-align: center; font-weight: 800; font-size: 64px; line-height: 1.4; color: rgba(245,241,234,0.8); }
    #s04-lB { position: absolute; left: 40px; right: 40px; top: 1335px; text-align: center; font-weight: 800; font-size: 112px; line-height: 1.35; }'''
html = f'''      <div class="s04-tag" id="s04-tag">DISTINCTIVE<b>02</b></div>
      <div id="s04-h" class="s04-ar">{words(p,'a','أبل: تفاحة معضوضة.',orange=(0,2))}</div>
      <svg id="s04-geo" viewBox="0 0 24 24">
        <g fill="none" stroke="#f5f1ea" stroke-opacity="0.3" stroke-width="0.06">
          <circle id="s04-g1" cx="8.1" cy="14.6" r="7.3" /><circle id="s04-g2" cx="15.2" cy="14.6" r="7.3" />
        </g>
        <circle id="s04-bite" cx="21.9" cy="10.4" r="3.1" fill="none" stroke="#ff4d1a" stroke-width="0.12" />
      </svg>
      <svg id="s04-art" viewBox="0 0 24 24"><path fill="#f5f1ea" d="{APPLE}"/></svg>
      <div id="s04-word"><span id="s04-wordin">Apple<i id="s04-wx"></i></span></div>
      <div id="s04-lA" class="s04-ar">{words(p,'b','حتى بلا اسم،')}</div>
      <div id="s04-lB" class="s04-ar">{words(p,'c','بتعرف مين.',orange=(1,))}</div>'''
js = '''      tl.fromTo("#s04-tag", { opacity: 0, x: 24 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, 0.05);
      seq("#s04-a", [0, 0.453, 0.929]);
      tl.fromTo("#s04-art", { opacity: 0, scale: 0.82, transformOrigin: "50% 60%" }, { opacity: 1, scale: 1, duration: 0.6, ease: "expo.out" }, 0.05);
      tl.fromTo("#s04-wordin", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, 0.25);
      tl.fromTo(["#s04-g1", "#s04-g2"], { scale: 0, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1, opacity: 1, duration: 0.6, ease: "expo.out", stagger: 0.12 }, V + 0.4);
      // "معضوضة" — the bite is the idea
      tl.fromTo("#s04-bite", { scale: 0, transformOrigin: "50% 50%" }, { scale: 1, duration: 0.5, ease: "back.out(2.2)" }, V + 0.93);
      // "حتى بلا اسم،" — the name is struck and wiped
      seq("#s04-b", [1.683, 2.067, 2.241]);
      tl.fromTo("#s04-wx", { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power3.inOut" }, V + 1.75);
      tl.to("#s04-wordin", { clipPath: "inset(-20% 0% -20% 100%)", duration: 0.45, ease: "expo.inOut" }, V + 2.2);
      // "بتعرف مين."
      tl.to("#s04-geo", { opacity: 0, duration: 0.4 }, V + 2.5);
      tl.to("#s04-lA", { opacity: 0.4, duration: 0.3 }, V + 2.55);
      word("#s04-c1", V + 2.589);
      pop("#s04-c2", V + 3.03);
      tl.to("#s04-art", { scale: 1.06, y: 30, duration: 1.0, ease: "expo.out" }, V + 2.6);'''
W('s04-apple', frame('s04-apple', p, 3.9, css, html, js, 0.2))

# ---------------- s05 mcdonald's ----------------
p='s05'
css = base_css(p, ['k800','p600','i700','i800']) + '''
    #s05-h { position: absolute; left: 60px; right: 90px; top: 372px; text-align: right; font-weight: 800; font-size: 90px; line-height: 1.4; }
    #s05-road { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: visible; }
    #s05-arch { position: absolute; left: 310px; top: 600px; width: 460px; height: 460px; overflow: visible; }
    #s05-chips { position: absolute; left: 90px; right: 90px; top: 1120px; height: 100px; }
    .s05-chip { position: absolute; top: 0; height: 90px; padding: 0 30px; border: 1.5px solid rgba(245,241,234,0.25); border-radius: 45px; direction: rtl; white-space: nowrap; font-family: "Noto Kufi Arabic", sans-serif; font-weight: 800; font-size: 40px; line-height: 86px; }
    .s05-chip small { font-family: "Inter", sans-serif; font-weight: 800; font-size: 20px; letter-spacing: 0.2em; color: rgba(245,241,234,0.5); margin-right: 18px; vertical-align: 4px; }
    .s05-chip i { display: inline-block; width: 26px; height: 26px; border-radius: 50%; margin-left: 16px; vertical-align: -3px; }
    #s05-q1 { right: 0; } #s05-q1 i { border: 3px solid #ff4d1a; }
    #s05-q2 { left: 0; } #s05-q2 i { background: #ffb000; }
    #s05-end { position: absolute; left: 40px; right: 40px; top: 1320px; text-align: center; font-weight: 800; font-size: 84px; line-height: 1.4; }'''
html = f'''      <div class="s05-tag" id="s05-tag">RECOGNIZABLE<b>03</b></div>
      <div id="s05-h" class="s05-ar">{words(p,'a','ماكدونالدز:',orange=(0,))}</div>
      <svg id="s05-road" viewBox="0 0 1080 1920">
        <g stroke="#f5f1ea" stroke-opacity="0.25" stroke-width="2" fill="none">
          <line id="s05-r1" x1="40" y1="1300" x2="530" y2="760" stroke-dasharray="730" stroke-dashoffset="730" />
          <line id="s05-r2" x1="1040" y1="1300" x2="550" y2="760" stroke-dasharray="730" stroke-dashoffset="730" />
        </g>
        <g id="s05-dash" stroke="#ff4d1a" stroke-width="5" stroke-linecap="round">
          <line x1="540" y1="1290" x2="540" y2="1220" /><line x1="540" y1="1150" x2="540" y2="1100" /><line x1="540" y1="1040" x2="540" y2="1005" /><line x1="540" y1="955" x2="540" y2="932" /><line x1="540" y1="890" x2="540" y2="876" />
        </g>
      </svg>
      <svg id="s05-arch" viewBox="0 0 24 24"><path fill="#ffb000" d="{MCD}"/></svg>
      <div id="s05-chips">
        <div class="s05-chip" id="s05-q1"><i></i>شكل واضح<small>SHAPE</small></div>
        <div class="s05-chip" id="s05-q2"><i></i>لون قوي<small>COLOR</small></div>
      </div>
      <div id="s05-end" class="s05-ar">{words(p,'e','بتعرفو من آخر الطريق.',orange=(2,3))}</div>'''
js = '''      tl.fromTo("#s05-tag", { opacity: 0, x: 24 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, 0.05);
      word("#s05-a1", V + 0);
      tl.fromTo("#s05-arch", { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.9, ease: "expo.inOut" }, 0.05);
      pop("#s05-q1", V + 1.09);
      pop("#s05-q2", V + 1.96);
      tl.to("#s05-arch", { scale: 1.05, duration: 0.5, ease: "power2.out", transformOrigin: "50% 100%" }, V + 2.35);
      // "بتعرفو من آخر الطريق." — the arches recede to the horizon and still read
      tl.to("#s05-chips", { opacity: 0, y: -16, duration: 0.3, ease: "power2.in" }, V + 2.8);
      tl.to(["#s05-r1", "#s05-r2"], { strokeDashoffset: 0, duration: 0.8, ease: "power2.out" }, V + 2.9);
      tl.fromTo("#s05-dash", { opacity: 0 }, { opacity: 1, duration: 0.5 }, V + 3.1);
      tl.to("#s05-arch", { scale: 0.16, y: -80, duration: 1.1, ease: "expo.inOut", transformOrigin: "50% 50%" }, V + 2.95);
      seq("#s05-e", [2.984, 3.448]);
      pop("#s05-e3", V + 3.576); pop("#s05-e4", V + 3.878);'''
W('s05-mcdonalds', frame('s05-mcdonalds', p, 4.9, css, html, js, 0.2))
print('a ok')
