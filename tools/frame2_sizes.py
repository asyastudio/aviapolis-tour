"""Точные размеры из Figma Frame 2 (макет 1440) + видео с Pexels на первом экране."""
import os, re
from fontTools.ttLib import TTFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = r'D:\google-drive\!Работа\!Авиаполис\ШРИФТ\Aviapolis\Aviapolis Regular.otf'
t = TTFont(FONT); t.flavor = 'woff2'; t.save(os.path.join(ROOT, 'assets', 'fonts', 'aviapolis-regular.woff2'))

def v(px, lo=None):
    """px в макете 1440 -> масштаб по ширине, не больше px и не меньше lo"""
    s = f'{px/14.4:.3f}vw'
    return f'clamp({lo}px,{s},{px}px)' if lo else f'min({px}px,{s})'

VIDEO = ('<video class="hero-video2" autoplay muted loop playsinline preload="auto" poster="assets/img/hero-taiga.webp" aria-hidden="true">'
         '<source src="assets/video/hero-taiga.mp4" type="video/mp4"></video>')
for page in ('tri-stihii-urala.html', 'index.html'):
    p = os.path.join(ROOT, page); s = open(p, encoding='utf-8').read()
    s = re.sub(r'<div class="hero-yt" aria-hidden="true">.*?</div>', VIDEO, s, flags=re.S)
    open(p, 'w', encoding='utf-8').write(s)

common = f'''
/* ===== FRAME 2 — exact sizes (1440 layout) ===== */
@font-face{{font-family:"Aviapolis";src:url("../fonts/aviapolis-regular.woff2") format("woff2");font-weight:400;font-display:swap}}
.hero-video2{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0}}
'''
tour = common + f'''
.hero-f2>.hero-video2{{position:absolute!important;z-index:0!important}}
.hero-f2{{min-height:{v(860,560)}!important;height:auto!important;justify-content:flex-start!important}}
.hero-f2 .hero-main{{padding-top:{v(245,130)}!important;padding-bottom:{v(120,48)}!important}}
.hero-f2 h1{{font-size:{v(104,44)}!important;line-height:.88!important;letter-spacing:0!important;margin:0!important}}
.hero-f2 .hero-desc{{font-weight:400!important;font-size:{v(29,16)}!important;line-height:1.2!important;max-width:{v(681,300)}!important;margin:{v(25,14)} auto 0!important}}
.hero-f2 .hero-links{{margin-top:{v(47,28)}!important}}
.hero-f2 .hero-cta{{font-size:{v(19,16)}!important;padding:{v(14,12)} {v(24,20)}!important}}

.expect{{padding-top:{v(76,48)}!important}}
.expect .exp-title{{font-size:{v(57,28)}!important;line-height:1.06!important;max-width:{v(1041,320)}!important}}
.fan{{margin-top:{v(72,36)}!important;gap:0!important;max-width:none!important}}
.fan-card{{width:{v(419,220)}!important;aspect-ratio:419/598!important;border-radius:24px 24px 24px 0!important}}
.fan-card.c1{{transform:translateY({v(33)}) rotate(-7deg)!important}}
.fan-card.c2{{transform:none!important}}
.fan-card.c3{{transform:translateY({v(36)}) rotate(8deg)!important}}
.fan-card:hover{{transform:translateY(-10px) rotate(0)!important}}
.fan-card figcaption{{padding:0 {v(26,18)} {v(28,20)}!important}}
.fan-tag{{font-size:{v(24,15)}!important}}
.fan-card b{{font-size:{v(26,18)}!important}}
.fan-card figcaption>span:last-child{{font-size:{v(19,14)}!important}}
.exp-lead{{margin-top:{v(82,40)}!important;font-size:{v(34,19)}!important;line-height:1.3!important;max-width:{v(781,320)}!important;margin-inline:auto!important}}
.facts{{margin-top:{v(84,48)}!important;padding-bottom:{v(112,56)}!important;max-width:1300px!important;gap:{v(40,24)}!important}}
.glass-ico{{width:{v(80,64)}!important;height:{v(80,64)}!important}}
.glass-ico svg{{width:{v(46,38)}!important;height:{v(46,38)}!important}}
.fact{{gap:0!important}}
.fact h3{{font-size:{v(35,22)}!important;margin-top:{v(19,12)}!important}}
.fact p{{font-size:{v(21,15)}!important;line-height:1.1!important;letter-spacing:.01em;margin-top:{v(9,6)}!important;max-width:{v(345,240)}!important}}
#route{{padding-top:{v(61,40)}!important}}
#route h2{{font-size:{v(50,30)}!important}}
@media (max-width:900px){{.fan-card.c1,.fan-card.c3{{transform:none!important}}}}
'''
open(os.path.join(ROOT, 'assets', 'css', 'tour.css'), 'a', encoding='utf-8').write(tour)
home = common + '''
.hf2>.hero-video2{position:absolute;z-index:0}
.hf2 p{font-family:"Aviapolis",var(--f-body)!important;font-weight:400!important}
'''
open(os.path.join(ROOT, 'assets', 'css', 'home.css'), 'a', encoding='utf-8').write(home)
print('ok')
