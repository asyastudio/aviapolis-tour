"""Подробная программа как в Figma «Program — ровный вариант»: фото и карточка 606×380 в шахматку,
вкладка дня с меткой на фото, единый текст (Aviapolis), пунктирные связи между днями."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'tri-stihii-urala.html'); s = open(P, encoding='utf-8').read()
def v(px, lo=None):
    q = f'{px/14.4:.3f}vw'
    return f'clamp({lo}px,{q},{px}px)' if lo is not None else f'min({px}px,{q})'

PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'
days = [
 ('1', 'mountains.webp', 'Скалы Бойцы над Чусовой', 'Плеханово, первый полёт<br>и база у озера',
  ['Утром брифинг на аэродроме Плеханово и вылет. Под крылом Невьянское водохранилище, Невьянская башня, хребты и Скалы Бойцы вдоль Чусовой.',
   'Обедаем на базе в лесу у озера. Днём квадроциклы или внедорожники, по погоде. Вечером баня, озеро, уральская кухня, костёр и разговор с пилотом.'],
  'Размещение: база у озера', ''),
 ('2', 'kayak.webp', 'Сплав по Чусовой', 'Лысьва, Кын и сплав<br>по Чусовой',
  ['Инструктаж на аэродроме Лысьвы и полёт в сторону Кына. Сплав по Чусовой: река, скалы, Камень Великан и старая советская метеостанция.',
   'Вечером ужин первой экспедиции, памятные сувениры и разговор о следующих маршрутах.'],
  'Размещение: база у озера', ' rev'),
 ('3', 'fishing.webp', 'Рыбалка на рассвете', 'Рыбалка и полёт над хребтом',
  ['Рыбалка с подготовленными снастями. После завтрака едем на аэродром Лысьвы: смотрим технику, знакомимся с самолётом.',
   'Обратный полёт над Уральским хребтом в Плеханово и трансфер в Тюмень с гидом-историком.'],
  'Финиш: Тюмень', ''),
]
rows = []
for n, img, alt, title, ps, stay, rev in days:
    crop = ' style="object-position:18% 100%"' if img == 'fishing.webp' else ''
    body = ''.join(f'<p>{x}</p>' for x in ps)
    rows.append(f'''      <article class="pday{rev}">
        <figure class="pday-img"><img loading="lazy" src="assets/img/{img}" alt="{alt}"{crop}><span class="pday-tab">{PIN}День {n}</span></figure>
        <div class="pday-card"><h3>{title}</h3>{body}<span class="pday-stay">{stay}</span></div>
      </article>''')
arcs = ('<svg class="pday-link r" viewBox="0 0 60 440" preserveAspectRatio="none" aria-hidden="true"><path d="M2 10 C58 60 58 380 2 430"/></svg>'
        '<svg class="pday-link l" viewBox="0 0 60 440" preserveAspectRatio="none" aria-hidden="true"><path d="M58 10 C2 60 2 380 58 430"/></svg>')
new = f'''<section id="program" class="prog2">
  <div class="wrap">
    <h2 class="prog2-title">Подробная программа</h2>
    <p class="prog2-sub">Три дня, три стихии</p>
    <div class="pdays">{arcs}
{chr(10).join(rows)}
    </div>
  </div>
</section>'''
s = re.sub(r'<section id="program">.*?</section>', new, s, count=1, flags=re.S)
open(P, 'w', encoding='utf-8').write(s)

css = f'''
/* ===== PROGRAM v2 (Figma «Program — ровный вариант») ===== */
main>section#program.prog2{{background:#F6FAFF!important;color:#0A1E40!important;padding-block:{v(93,56)} {v(110,56)}!important}}
.prog2 .bps{{display:none!important}}
.prog2-title{{font-family:var(--f-accent)!important;font-size:{v(56,32)}!important;line-height:1.1!important;color:#0043BF!important;text-align:center;margin:0!important}}
.prog2-sub{{text-align:center;margin:{v(10,6)} 0 0!important;font-family:var(--f-body);font-weight:700;font-size:{v(29,18)}!important;letter-spacing:.01em;text-transform:uppercase;color:#0A1E40!important;max-width:none!important}}
.pdays{{position:relative;display:grid;gap:40px;max-width:1236px;margin:{v(56,32)} auto 0}}
.pday{{display:grid;grid-template-columns:1fr 1fr;gap:24px;min-height:{v(380,0)}}}
.pday.rev .pday-img{{order:2}}
.pday-img,.pday-card{{border-radius:24px 24px 24px 0;overflow:hidden;box-shadow:0 22px 50px rgba(0,40,120,.12)}}
.pday-img{{position:relative;margin:0;min-height:{v(380,240)}}}
.pday-img img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.pday-tab{{position:absolute;top:30px;left:33px;display:inline-flex;align-items:center;gap:8px;height:52px;padding:0 20px 0 16px;border-radius:16px 16px 16px 0;background:#00A6FF;color:#fff;font-family:var(--f-accent);font-weight:700;font-size:20px}}
.pday.rev .pday-tab{{left:auto;right:33px}}
.pday-tab svg{{width:22px;height:22px;fill:#fff}}
.pday-card{{background:#fff;padding:30px 40px;display:flex;flex-direction:column}}
.pday-card h3{{font-family:var(--f-accent)!important;font-weight:700;font-size:{v(35,24)}!important;line-height:1.12!important;color:#0A1E40!important;margin:0 0 18px!important;text-wrap:balance}}
.pday-card p{{font-family:var(--f-accent)!important;font-weight:400;font-size:{v(20,16)}!important;line-height:1.09!important;color:#0A1E40!important;margin:0 0 17px!important;max-width:none!important}}
.pday-stay{{margin-top:auto;padding-top:14px;border-top:1px solid #DCE8F4;font-family:var(--f-accent);font-size:{v(20,16)};color:#0A1E40}}
.pday-link{{position:absolute;width:60px;pointer-events:none;overflow:visible}}
.pday-link path{{fill:none;stroke:#00A6FF;stroke-width:2.4;stroke-linecap:round;stroke-dasharray:10 11;vector-effect:non-scaling-stroke}}
.pday-link.r{{right:-58px;top:calc((100% - 80px)/6 - 10px);height:calc((100% - 80px)/3 + 60px)}}
.pday-link.l{{left:-58px;top:calc((100% - 80px)/2 + 30px);height:calc((100% - 80px)/3 + 60px)}}
@media (max-width:1300px){{.pday-link{{display:none}}}}
@media (max-width:820px){{.pday{{grid-template-columns:1fr}}.pday.rev .pday-img{{order:0}}.pday-card{{padding:24px}}}}
'''
open(os.path.join(ROOT, 'assets', 'css', 'tour.css'), 'a', encoding='utf-8').write(css)
print('ok')
