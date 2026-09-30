"""Переносит дизайн из Figma (Frame 2) на страницу маршрута: первый экран, блок «Урал…», факты, метки маршрута."""
import os, re
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'tri-stihii-urala.html')
CSS = os.path.join(ROOT, 'assets', 'css', 'tour.css')
BANK = r'D:\google-drive\!Работа\!Авиаполис\Сайт Авиаполис Тур\Фото банк'

# hero photo (poster for the kayak loop)
im = Image.open(os.path.join(BANK, 'canoeist-lake-alps.jpg')).convert('RGB')
im.thumbnail((2000, 2000))
im.save(os.path.join(ROOT, 'assets', 'img', 'hero-kayak.webp'), 'WEBP', quality=80, method=6)

s = open(P, encoding='utf-8').read()

# ---------- HERO ----------
hero_old = re.search(r'<header class="hero" id="top">.*?</header>', s, re.S).group(0)
hero_new = '''<header class="hero hero-f2" id="top">
  <div class="hero-bg" role="img" aria-label="Каяк на горном озере"></div>
  <div class="hero-yt" aria-hidden="true"><iframe src="https://www.youtube-nocookie.com/embed/lcZj-w_lTKw?autoplay=1&amp;mute=1&amp;loop=1&amp;playlist=lcZj-w_lTKw&amp;controls=0&amp;modestbranding=1&amp;playsinline=1&amp;rel=0&amp;disablekb=1&amp;iv_load_policy=3" title="Видео на первом экране" allow="autoplay; encrypted-media" tabindex="-1"></iframe></div>
  <div class="wrap hero-main">
    <h1>Три стихии Урала</h1>
    <p class="hero-desc">Три дня над Уралом на малом самолёте. Невьянская башня и Скалы Бойцы с высоты, сплав по Чусовой к Камню Великану, рыбалка на рассвете и баня у озера</p>
    <div class="hero-links"><a class="btn hero-cta" href="#apply">Забронировать место</a></div>
  </div>
</header>'''
s = s.replace(hero_old, hero_new)

# ---------- EXPECT ----------
exp = re.search(r'(<section class="expect" id="expect">(?:<div class="bps".*?</div>)?)\s*<div class="wrap">.*?</section>', s, re.S)
oval = ('<svg class="oval" viewBox="0 0 360 130" preserveAspectRatio="none" aria-hidden="true">'
        '<path d="M40 30C110 8 260 6 322 34c40 18 36 60-10 76-70 24-210 22-268-4C-4 84 8 44 64 26c50-16 150-18 210-10"/></svg>')
ico = {
 'sky': '<svg viewBox="0 0 64 64"><path d="M8 15v12"/><path d="M11 21c0-2 2-3 4-3h24l7-8h4l-1.5 11c0 2-1.5 3-3.5 3H15c-2 0-4-1-4-3z"/><path d="M19 14h20"/><path d="M26 14l2 4"/><path d="M20 24v3M36 24v3"/><path d="M6 48c4-4 8-4 12 0s8 4 12 0"/><path d="M49 32l-7 10h4l-5 8h16l-5-8h4z"/><path d="M49 50v6"/></svg>',
 'pin': '<svg viewBox="0 0 64 64"><path d="M32 58S15 42 15 28a17 17 0 0 1 34 0c0 14-17 30-17 30z"/><path d="M23 34l7-10 4 5 3-3 5 8z"/></svg>',
 'ok':  '<svg viewBox="0 0 64 64"><path d="M18 10h28a8 8 0 0 1 8 8v28a8 8 0 0 1-8 8H10V18a8 8 0 0 1 8-8z"/><path d="M22 33l7 7 14-15"/></svg>'}
def card(cls, img, alt, tag, title, desc):
    return (f'<figure class="fan-card {cls}"><img loading="lazy" src="assets/img/{img}" alt="{alt}">'
            f'<figcaption><span class="fan-tag">{tag}</span><b>{title}</b><span>{desc}</span></figcaption></figure>')
def fact(k, t, d):
    return f'<div class="fact"><span class="glass-ico">{ico[k]}</span><h3>{t}</h3><p>{d}</p></div>'
expect_inner = f'''
  <div class="wrap">
    <h2 class="exp-title">Урал, который вы давно хотели увидеть, можно облететь <span class="circled">за три дня{oval}</span></h2>
    <div class="fan">
      {card('c1','yellow-plane.webp','Малый самолёт над тайгой','Небо','Невьянск и хребет','Перелёты на малом самолёте над Невьянском и хребтом')}
      {card('c2','cliffs.webp','Скалы над Чусовой','Вода','Чусовая','Сплав по Чусовой к Камню Великану')}
      {card('c3','cabin.webp','Домик у озера в лесу','Лес','База у озера','Рыбалка на рассвете и баня у озера')}
    </div>
    <p class="exp-lead">Не нужно искать аэродром, пилота, базу и лодку.<br>Перелёты, сплав, рыбалка и вечер у костра<br><b>уже собраны в одну поездку.</b></p>
    <div class="facts">
      <svg class="facts-path" viewBox="0 0 1440 340" preserveAspectRatio="none" aria-hidden="true"><path d="M-20 320C200 300 300 180 460 250 560 295 470 360 430 300 390 240 560 150 760 170 980 190 1100 60 1460 10"/></svg>
      <svg class="facts-plane" viewBox="0 0 64 64" aria-hidden="true"><path d="M3 13l7-2 6-7 2 1-3 7 5 2-1 2-6-1-4 5H7l2-5-5-1z" transform="scale(2.6) rotate(-20 12 12)"/></svg>
      {fact('sky','3 стихии','перелёты на малом самолёте, сплав по Чусовой, рыбалка на рассвете и баня у озера')}
      {fact('pin','Топ-локации','Невьянская башня, Скалы Бойцы, река Чусовая и Камень Великан')}
      {fact('ok','Всё организовано','аэродром, пилот, база и лодка уже собраны в одну поездку')}
    </div>
  </div>
</section>'''
s = s[:exp.start()] + exp.group(1) + expect_inner + s[exp.end():]

# ---------- ROUTE LABELS ----------
s = s.replace('<span class="d">Старт · день 1</span>', '<span class="d">День 1</span>')
s = s.replace('<span class="d">Финиш · день 3</span>', '<span class="d">День 3</span>')
open(P, 'w', encoding='utf-8').write(s)

css = '''
/* ===== FRAME 2 DESIGN ===== */
.hero-f2 .hero-bg{background-image:url("../img/hero-kayak.webp")!important;background-position:center 60%!important;animation:none!important}
.hero-yt{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:0}
.hero-yt iframe{position:absolute;top:50%;left:50%;width:max(100%,177.78vh);height:max(100%,56.25vw);transform:translate(-50%,-50%);border:0}
.hero-f2>*:not(.hero-bg):not(.hero-yt){position:relative;z-index:1}
.hero-f2 .hero-main::before{display:none!important}
.hero-f2::after{background:linear-gradient(180deg,rgba(2,14,50,.35) 0%,rgba(2,14,50,0) 26%,rgba(2,14,50,0) 70%,rgba(2,14,50,.25) 100%)!important}
.hero-f2 h1{font-family:var(--f-accent)!important;font-size:clamp(46px,7.2vw,112px)!important;line-height:1!important;letter-spacing:.005em!important;white-space:nowrap;text-shadow:0 4px 30px rgba(0,20,60,.35)!important}
.hero-f2 .hero-desc{font-family:var(--f-accent)!important;font-size:clamp(15px,1.4vw,20px)!important;line-height:1.35!important;max-width:30em!important;text-shadow:0 1px 3px rgba(0,15,45,.6),0 2px 16px rgba(0,15,45,.5)!important}
.hero-f2 .hero-links{margin-top:clamp(40px,7vh,72px)!important}
.hero-f2 .hero-cta{background:#0043BF!important;border-radius:14px 14px 14px 0!important;padding:16px 26px!important;font-size:18px!important}
.hero-f2 .hero-cta::after{display:none}
.hero-f2 .hero-cta:hover{background:#FF8A33!important}
@media (max-width:640px){.hero-f2 h1{white-space:normal}}

.expect{background:linear-gradient(180deg,#0043BF 0%,#0A4ED0 40%,#1E8BF5 72%,#08A6FF 100%)!important;text-align:center!important;padding-block:clamp(56px,7vw,96px) 0!important;overflow:hidden}
.expect .exp-title{font-family:var(--f-accent)!important;font-size:clamp(30px,4vw,58px)!important;line-height:1.12!important;color:#fff;max-width:19em;margin:0 auto!important;text-wrap:balance}
.circled{position:relative;display:inline-block;white-space:nowrap;padding:0 .15em}
.circled .oval{position:absolute;left:-12%;top:-26%;width:124%;height:152%;overflow:visible;pointer-events:none}
.circled .oval path{fill:none;stroke:#FF8A33;stroke-width:5;stroke-linecap:round;stroke-dasharray:1400;stroke-dashoffset:1400;transition:stroke-dashoffset 1.4s cubic-bezier(.65,0,.35,1) .2s;vector-effect:non-scaling-stroke}
.circled.drawn .oval path{stroke-dashoffset:0}
.fan{display:flex;justify-content:center;align-items:center;margin:clamp(40px,5vw,64px) auto 0;max-width:1180px}
.fan-card{position:relative;margin:0;flex:0 0 auto;width:clamp(220px,26vw,380px);aspect-ratio:3/4.2;border-radius:28px 28px 28px 0;overflow:hidden;box-shadow:0 30px 60px rgba(0,20,80,.4);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.fan-card img{width:100%;height:100%;object-fit:cover;display:block}
.fan-card::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(4,14,44,.8) 0%,rgba(4,14,44,.35) 30%,rgba(4,14,44,0) 55%)}
.fan-card figcaption{position:absolute;left:0;right:0;bottom:0;z-index:1;padding:0 26px 28px;text-align:left;color:#fff;display:flex;flex-direction:column;gap:6px}
.fan-tag{align-self:flex-start;margin-bottom:6px;padding:6px 12px 4px;border-radius:10px 10px 10px 0;background:rgba(255,255,255,.22);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);font-family:var(--f-accent);font-size:clamp(16px,1.5vw,24px);letter-spacing:.06em;text-transform:uppercase;line-height:1}
.fan-card b{font-size:clamp(19px,1.8vw,26px);line-height:1.1}
.fan-card figcaption>span:last-child{font-size:clamp(14px,1.3vw,19px);line-height:1.3;opacity:.9}
.fan-card.c1{transform:rotate(-8deg) translate(22px,18px);z-index:1}
.fan-card.c2{transform:translateY(-8px);z-index:2}
.fan-card.c3{transform:rotate(9deg) translate(-22px,22px);z-index:1}
.fan-card:hover{transform:rotate(0) translateY(-14px) scale(1.03);z-index:3}
.exp-lead{max-width:none!important;margin:clamp(48px,6vw,80px) auto 0!important;font-size:clamp(20px,2.3vw,34px)!important;line-height:1.35!important;color:#fff!important;font-weight:400}
.exp-lead b{font-weight:700}
.facts{position:relative;display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin:clamp(56px,7vw,96px) auto 0;padding-bottom:clamp(64px,8vw,110px);max-width:1180px}
.facts-path{position:absolute;left:50%;bottom:0;width:100vw;height:340px;transform:translateX(-50%);overflow:visible;pointer-events:none}
.facts-path path{fill:none;stroke:rgba(255,255,255,.5);stroke-width:2;stroke-dasharray:7 9;vector-effect:non-scaling-stroke}
.facts-plane{position:absolute;right:-6%;top:-150px;width:clamp(90px,9vw,140px);fill:rgba(255,255,255,.28);transform:rotate(10deg)}
.fact{position:relative;display:flex;flex-direction:column;align-items:center;gap:14px}
.glass-ico{width:88px;height:88px;display:grid;place-items:center;border-radius:26px 26px 26px 0;background:linear-gradient(135deg,rgba(255,255,255,.42),rgba(255,255,255,.1));border:1.5px solid rgba(255,255,255,.55);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:0 16px 30px rgba(0,30,100,.22),inset 0 1px 0 rgba(255,255,255,.6)}
.glass-ico svg{width:52px;height:52px;fill:none;stroke:#fff;stroke-width:2.8;stroke-linecap:round;stroke-linejoin:round}
.fact h3{font-family:var(--f-accent)!important;font-size:clamp(24px,2.3vw,34px)!important;text-transform:uppercase;color:#fff!important;margin:6px 0 0!important;line-height:1}
.fact p{font-size:clamp(15px,1.3vw,19px);line-height:1.35;color:#fff;max-width:17em;margin:0}
@media (max-width:900px){.fan{flex-direction:column;gap:18px}.fan-card{width:min(360px,86vw)}.fan-card.c1,.fan-card.c2,.fan-card.c3{transform:none}.facts{grid-template-columns:1fr;gap:40px}.facts-plane{display:none}.exp-lead br{display:none}}

/* route labels as in Figma */
.road .stop .d{font-weight:700!important;font-size:15px!important;text-transform:uppercase!important;letter-spacing:.02em!important;-webkit-text-stroke:0!important}
'''
open(CSS, 'a', encoding='utf-8').write(css)

js = os.path.join(ROOT, 'assets', 'js', 'tour.js')
j = open(js, encoding='utf-8').read()
j = j.replace("v.addEventListener('canplay',function(){v.hidden=false;});", "v.addEventListener('canplay',function(){v.hidden=false;v.play&&v.play();});")
j += '''
(function(){var c=document.querySelector('.circled');if(!c)return;if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches){c.classList.add('drawn');return}
new IntersectionObserver(function(e,o){if(e[0].isIntersecting){c.classList.add('drawn');o.disconnect()}},{threshold:.6}).observe(c)})();
'''
open(js, 'w', encoding='utf-8').write(j)
print('ok')
