"""Главная в стиле Frame 2: шапка, первый экран с видео, фоны-градиенты, карточки маршрутов."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'index.html'); CSS = os.path.join(ROOT, 'assets', 'css', 'home.css')
s = open(P, encoding='utf-8').read()
s = s.replace('    <a class="btn-head" href="#apply">Забронировать место</a>\n',
              '    <a class="head-contact" href="tel:+70000000000">+7 (000) 000-00-00</a>\n    <a class="head-contact" href="mailto:mail@example.ru">mail@example.ru</a>\n')
hero_old = re.search(r'<header class="hero" id="top">.*?</header>', s, re.S).group(0)
hero_new = '''<header class="hero hf2" id="top">
  <div class="hf2-bg" aria-hidden="true"></div>
  <div class="hero-yt" aria-hidden="true"><iframe src="https://www.youtube-nocookie.com/embed/lcZj-w_lTKw?autoplay=1&amp;mute=1&amp;loop=1&amp;playlist=lcZj-w_lTKw&amp;controls=0&amp;modestbranding=1&amp;playsinline=1&amp;rel=0&amp;disablekb=1&amp;iv_load_policy=3" title="Видео на первом экране" allow="autoplay; encrypted-media" tabindex="-1"></iframe></div>
  <div class="wrap hf2-main">
    <h1>Россия с высоты малого самолёта</h1>
    <p>Собираем экспедиции целиком: перелёты между небольшими аэродромами, база, пилот, активности на земле и воде. Вам остаётся выбрать маршрут.</p>
    <div class="hf2-links"><a class="hf2-cta" href="#routes">Выбрать маршрут</a><a class="hf2-link" href="#apply">Свой маршрут</a></div>
  </div>
</header>'''
s = s.replace(hero_old, hero_new)
s = re.sub(r'<span class="eyebrow">[^<]*</span>', '', s)
open(P, 'w', encoding='utf-8').write(s)

css = '''
/* ===== FRAME 2 DESIGN (home) ===== */
.head::before{display:none!important}
.head{background:none!important;box-shadow:none!important}
.head-in{max-width:none!important;border-radius:0!important;border:0!important;border-bottom:1px solid rgba(255,255,255,.22)!important;padding:12px clamp(16px,4vw,64px)!important;background:rgba(6,28,80,.22)!important;backdrop-filter:blur(18px) saturate(1.3);-webkit-backdrop-filter:blur(18px) saturate(1.3);color:#fff!important}
.head.scrolled .head-in{background:rgba(2,14,60,.62)!important}
.head nav a,.head.scrolled nav a{color:#fff!important;font-size:15.5px!important;font-weight:400!important}
.head.scrolled .logo-light{display:block!important}.head.scrolled .logo-dark{display:none!important}
.head-cta{display:flex;gap:18px;align-items:center}
.head-contact{color:#fff;text-decoration:none;font-size:16px;white-space:nowrap}
.head .tg{background:rgba(255,255,255,.16)!important;border:0!important;color:#fff!important}
@media (max-width:1100px){.head-contact[href^="mailto"]{display:none}}
@media (max-width:640px){.head-contact{display:none}}

.hf2{position:relative;min-height:min(100vh,900px);display:flex;align-items:center;justify-content:center;overflow:hidden;color:#fff;text-align:center;background:#0B3A7A!important;padding:0!important}
.hf2-bg{position:absolute;inset:0;background:url("../img/hero-kayak.webp") center 60%/cover}
.hero-yt{position:absolute!important;inset:0;overflow:hidden;pointer-events:none;z-index:0}
.hero-yt iframe{position:absolute;top:50%;left:50%;width:max(100%,177.78vh);height:max(100%,56.25vw);transform:translate(-50%,-50%);border:0}
.hf2::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(2,14,50,.35) 0%,rgba(2,14,50,0) 26%,rgba(2,14,50,0) 70%,rgba(2,14,50,.3) 100%);pointer-events:none}
.hf2-main{position:relative;z-index:1;padding-top:80px}
.hf2 h1{font-family:var(--f-accent)!important;font-size:clamp(40px,6vw,96px)!important;line-height:1.02!important;max-width:12em;margin:0 auto!important;color:#fff!important;text-wrap:balance;text-shadow:0 4px 30px rgba(0,20,60,.35)}
.hf2 p{font-family:var(--f-accent);font-size:clamp(15px,1.4vw,20px);line-height:1.35;max-width:30em;margin:22px auto 0;color:#fff;text-shadow:0 1px 3px rgba(0,15,45,.6),0 2px 16px rgba(0,15,45,.5)}
.hf2-links{display:flex;gap:28px;justify-content:center;align-items:center;margin-top:clamp(40px,7vh,72px)}
.hf2-cta{display:inline-flex;padding:16px 26px;border-radius:14px 14px 14px 0;background:#0043BF;color:#fff;font-weight:700;font-size:18px;text-decoration:none;transition:background .3s,transform .3s}
.hf2-cta:hover{background:#FF8A33;transform:translateY(-2px)}
.hf2-link{color:#fff;font-size:18px;text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1px}

main>section:not(.safety){background:linear-gradient(180deg,#0043BF 0%,#0A4ED0 45%,#1E8BF5 80%,#08A6FF 100%)!important;color:#fff}
main>section:not(.safety):nth-of-type(even){background:linear-gradient(180deg,#08A6FF 0%,#1E8BF5 25%,#0A4ED0 60%,#0043BF 100%)!important}
main>section h2{font-family:var(--f-accent)!important;color:#fff!important}
main>section:not(.safety) p,main>section:not(.safety) .routes-head p{color:#fff}
.rc{border-radius:28px 28px 28px 0!important;box-shadow:0 30px 60px rgba(0,20,80,.35)!important}
.grid2>.rc:first-child{transform:rotate(-3deg)}
.grid2>.rc:nth-child(3){transform:rotate(3deg)}
.grid2>.rc:hover{transform:rotate(0) translateY(-8px)!important}
'''
open(CSS, 'a', encoding='utf-8').write(css)
print('ok')
