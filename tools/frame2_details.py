"""Детали из Figma Frame 2: шапка на всю ширину с новым логотипом, прямые карточки лесенкой,
точные иконки фактов, фоны как в макете, точные отступы (макет 1440)."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = r'D:\google-drive\!Работа\!Авиаполис\Сайт Авиаполис Тур\Варианты логотипа\Авиаполис-Тур-рукописный.svg'
IMG = os.path.join(ROOT, 'assets', 'img')

svg = open(SRC, encoding='utf-8').read()
svg = re.sub(r'<\?xml[^>]*>\s*', '', svg)
open(os.path.join(IMG, 'logo-tour.svg'), 'w', encoding='utf-8').write(svg)
open(os.path.join(IMG, 'logo-tour-white.svg'), 'w', encoding='utf-8').write(svg.replace('#0043BF', '#FFFFFF').replace('#00A6FF', '#FFFFFF'))

def v(px, lo=None):
    s = f'{px/14.4:.3f}vw'
    return f'clamp({lo}px,{s},{px}px)' if lo is not None else f'min({px}px,{s})'

ICONS = {
 'sky': '<path d="M6.04175 11.3281V20.3906"/><path d="M8.30737 15.859C8.30737 14.3486 9.81779 13.5934 11.3282 13.5934H29.4532L34.7397 7.55176H37.7605L36.6277 15.859C36.6277 17.3695 35.4949 18.1247 33.9845 18.1247H11.3282C9.81779 18.1247 8.30737 17.3695 8.30737 15.859Z"/><path d="M14.3489 10.5723H29.453"/><path d="M19.6355 10.5723L21.1459 13.5931"/><path d="M15.1042 18.125V20.3906M27.1876 18.125V20.3906"/><path d="M4.53125 36.25C7.55208 33.2292 10.5729 33.2292 13.5937 36.25C16.6146 39.2708 19.6354 39.2708 22.6562 36.25"/><path d="M37.0053 24.166L31.7188 31.7181H34.7397L30.9636 37.7598H43.047L39.2709 31.7181H42.2917L37.0053 24.166Z"/><path d="M37.0051 37.7598V42.291"/>',
 'pin': '<path d="M24.1667 43.8024C24.1667 43.8024 11.3281 31.7191 11.3281 21.1462C11.3281 17.7412 12.6808 14.4756 15.0884 12.0679C17.4961 9.66025 20.7617 8.30762 24.1667 8.30762C27.5717 8.30762 30.8372 9.66025 33.2449 12.0679C35.6526 14.4756 37.0052 17.7412 37.0052 21.1462C37.0052 31.7191 24.1667 43.8024 24.1667 43.8024Z"/><path d="M17.3699 25.6771L22.6563 18.125L25.6772 21.901L27.9428 19.6354L31.7188 25.6771H17.3699Z"/>',
 'ok': '<path d="M13.5937 7.55176H34.7395C36.3418 7.55176 37.8786 8.18829 39.0116 9.32132C40.1446 10.4544 40.7812 11.9911 40.7812 13.5934V34.7393C40.7812 36.3416 40.1446 37.8783 39.0116 39.0114C37.8786 40.1444 36.3418 40.7809 34.7395 40.7809H7.552V13.5934C7.552 11.9911 8.18853 10.4544 9.32156 9.32132C10.4546 8.18829 11.9913 7.55176 13.5937 7.55176Z"/><path d="M16.6145 24.9215L21.901 30.208L32.4739 18.8799"/>'}
FACT_P = ['перелёты на малом самолёте,<br>сплав по Чусовой, рыбалка на<br>рассвете и баня у озера',
          'Невьянская башня, Скалы<br>Бойцы, река Чусовая<br>и Камень Великан',
          'аэродром, пилот, база<br>и лодка уже собраны в<br>одну поездку']
LOGO = '<a class="brand" href="{href}" aria-label="Авиаполис-Тур"><img class="logo-tour" src="assets/img/logo-tour-white.svg" alt="Авиаполис-Тур"></a>'

for page, href in (('tri-stihii-urala.html', 'index.html'), ('index.html', '#top')):
    p = os.path.join(ROOT, page); s = open(p, encoding='utf-8').read()
    s = re.sub(r'<a class="brand"[^>]*>.*?</a>', LOGO.format(href=href), s, count=1, flags=re.S)
    if page == 'tri-stihii-urala.html':
        # remove blurred planes in expect and route (not in the mockup)
        s = re.sub(r'(<section class="(?:expect|short)" id="(?:expect|route)">)<div class="bps" aria-hidden="true">.*?</div>', r'\1', s, flags=re.S)
        # exact icons
        for k in ('sky', 'pin', 'ok'):
            pass
        icons = re.findall(r'<span class="glass-ico"><svg viewBox="0 0 64 64">.*?</svg></span>', s, re.S)
        for old, k in zip(icons, ('sky', 'pin', 'ok')):
            s = s.replace(old, f'<span class="glass-ico"><svg viewBox="0 0 49 49">{ICONS[k]}</svg></span>', 1)
        ps = re.findall(r'(<div class="fact">.*?<h3>[^<]*</h3>)<p>[^<]*</p>', s, re.S)
        for (head), txt in zip(ps, FACT_P):
            s = re.sub(re.escape(head) + r'<p>[^<]*</p>', head.replace('\\', '\\\\') + f'<p>{txt}</p>', s, count=1)
    open(p, 'w', encoding='utf-8').write(s)

header = f'''
/* ===== FRAME 2 details: header ===== */
.head{{padding:0!important}}
.head-in{{display:flex!important;align-items:center;max-width:none!important;height:69px;min-height:0!important;padding:0 {v(63,16)} 0 {v(21,12)}!important;border-radius:0!important;border:0!important;border-bottom:1px solid rgba(255,255,255,.22)!important;background:rgba(19,19,19,.22)!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;gap:0!important}}
.head.scrolled .head-in{{background:rgba(19,19,19,.55)!important}}
.brand{{flex:none;margin:0!important;display:flex;align-items:center}}
.brand img{{display:none!important}}
.brand img.logo-tour{{display:block!important;width:171px;height:auto}}
.head nav{{display:flex!important;gap:60px!important;margin-left:{v(193,24)}!important;height:auto!important;padding:0!important;background:none!important;border:0!important}}
.head nav a,.head.scrolled nav a{{font-family:var(--f-body)!important;font-size:18px!important;font-weight:400!important;color:#fff!important;padding:0!important;opacity:1!important;letter-spacing:0!important}}
.head-cta{{margin-left:auto!important;display:flex;align-items:center;gap:18px!important}}
.head .tg,.head.scrolled .tg{{width:40px!important;height:40px!important;background:none!important;border:0!important;color:#fff!important;border-radius:0!important}}
.head .tg svg{{width:22px;height:22px}}
.head-contact{{font-family:var(--f-body);font-size:18px!important;font-weight:400;color:#fff!important}}
@media (max-width:1100px){{.head nav{{gap:28px!important;margin-left:32px!important}}}}
@media (max-width:900px){{.head nav{{display:none!important}}}}
'''
tour = header + f'''
/* ===== FRAME 2 details: sections ===== */
.hero-f2{{min-height:{v(843,540)}!important}}
.hero-f2 .hero-main{{padding-top:{v(245,120)}!important}}
.hero-f2 .hero-links{{margin-top:{v(49,28)}!important}}
.marquee{{height:33px;box-sizing:border-box;padding-block:0!important;display:flex;align-items:center}}

.expect{{padding-top:{v(60,40)}!important;background:
  radial-gradient(60% 18% at 50% 64%,rgba(0,166,255,.55),rgba(0,166,255,0) 70%),
  linear-gradient(180deg,#0A2A6B 0%,#003DB0 5%,#0040B5 50%,#0052C3 60%,#0079E9 68%,#00A6FF 78%,#00A6FF 100%)!important}}
.expect .bps{{display:none!important}}
.fan{{align-items:flex-start!important;justify-content:center!important;margin-top:{v(19,24)}!important;gap:{v(52,16)}!important}}
.fan-card{{width:{v(360,220)}!important;aspect-ratio:360/515!important;border-radius:24px 24px 24px 0!important;box-shadow:0 24px 50px rgba(0,20,80,.35)!important}}
.fan-card.c1,.fan-card.c2,.fan-card.c3{{transform:none!important}}
.fan-card.c1{{margin-top:{v(15,0)}!important}}
.fan-card.c2{{margin-top:{v(60,0)}!important}}
.fan-card.c3{{margin-top:0!important}}
.fan-card:hover{{transform:translateY(-8px)!important}}
.fan-card::after{{background:linear-gradient(0deg,rgba(4,14,44,.78) 0%,rgba(4,14,44,.4) 25%,rgba(4,14,44,0) 40%)!important}}
.fan-card figcaption{{padding:0 22px 22px!important;gap:8px!important}}
.fan-tag{{height:40px;box-sizing:border-box;display:inline-flex;align-items:center;padding:0 14px!important;font-size:20px!important;border-radius:10px 10px 10px 0!important;margin-bottom:4px!important;background:rgba(255,255,255,.2)!important}}
.fan-card b{{font-size:24px!important;line-height:1.1}}
.fan-card figcaption>span:last-child{{font-size:16px!important;line-height:1.25!important}}
.exp-lead{{margin-top:{v(56,32)}!important}}
.facts{{margin-top:{v(51,32)}!important;padding-bottom:{v(127,56)}!important;max-width:1312px!important;gap:0!important}}
.glass-ico{{width:80px!important;height:80px!important;border-radius:28px 28px 28px 0!important;background:linear-gradient(180deg,rgba(255,255,255,.42),rgba(255,255,255,.1))!important;border:1.5px solid rgba(255,255,255,.6)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important;box-shadow:0 16px 30px rgba(0,40,120,.25),inset 0 1px 0 rgba(255,255,255,.5)!important}}
.glass-ico svg{{width:48px!important;height:48px!important;fill:none;stroke:#fff;stroke-width:2.8;stroke-linecap:round;stroke-linejoin:round}}
.fact h3{{margin-top:19px!important;line-height:41px!important}}
.fact p{{margin-top:9px!important;font-size:21px!important;line-height:23px!important;max-width:none!important;letter-spacing:.01em}}
#route{{padding-top:{v(180,56)}!important;background:linear-gradient(180deg,#0043BF 0%,#0043BF 40%,#0A55D0 100%)!important}}
#route .bps{{display:none!important}}
'''
open(os.path.join(ROOT, 'assets', 'css', 'tour.css'), 'a', encoding='utf-8').write(tour)
open(os.path.join(ROOT, 'assets', 'css', 'home.css'), 'a', encoding='utf-8').write(header)

pv = os.path.join(ROOT, 'tools', 'preview.py'); t = open(pv, encoding='utf-8').read()
if "'svg'" not in t:
    t = t.replace("MT={'webp':'image/webp'", "MT={'svg':'image/svg+xml','webp':'image/webp'").replace(r"assets/img/[\w.-]+\.(?:webp|png|jpg)", r"assets/img/[\w.-]+\.(?:webp|png|jpg|svg)")
    open(pv, 'w', encoding='utf-8').write(t)
print('ok')
