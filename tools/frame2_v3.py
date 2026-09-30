"""Правки Frame 2 (третья версия): логотип по центру, заголовок в две строки с крупным «УРАЛА»,
карточки теснее, самолётик с пунктиром сверху, летнее видео."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def v(px, lo=None):
    s = f'{px/14.4:.3f}vw'
    return f'clamp({lo}px,{s},{px}px)' if lo is not None else f'min({px}px,{s})'

DECOR = ('<svg class="exp-decor" viewBox="0 0 978 410" fill="none" aria-hidden="true"><g opacity="0.5">'
 '<path d="M1.60019 406.473C189.713 420.872 262.839 275.18 403.918 289.507C509.729 299.076 521.353 386.106 448.451 385.994C375.549 385.883 380.419 277.713 486.291 247.303C613.336 212.223 719.223 172.407 846.318 104.404" stroke="white" stroke-opacity="0.39" stroke-width="3.2" stroke-linecap="round" stroke-dasharray="10 12"/>'
 '<path fill-rule="evenodd" clip-rule="evenodd" d="M945.639 64.6941C945.387 65.0544 944.889 65.1 944.6 64.7727L939.121 58.4574C938.724 58.001 937.925 58.2478 937.754 58.8255C936.812 61.3516 933.857 63.8123 927.924 66.6963C927.75 66.7899 927.515 66.7684 927.352 66.6726L925.393 65.6074C925.393 65.6074 925.082 65.5151 924.935 65.5202C923.467 65.9076 921.264 67.1406 922.506 69.6369C923.811 72.2483 940.216 104.196 948.565 120.407C948.708 120.739 948.602 121.094 948.301 121.295L939.499 125.7C939.21 125.855 938.855 125.75 938.699 125.462L904.597 77.6756C904.597 77.6756 904.116 77.3395 903.842 77.4521L893.443 81.044C893.111 81.187 892.902 81.5598 893.047 81.8936L899.335 98.3636C899.478 98.6961 899.315 99.083 898.938 99.2133L894.157 100.988C893.881 101.099 893.57 101.007 893.4 100.763L884.493 87.5796C884.493 87.5796 884.331 87.1448 884.429 86.9804L885.447 84.5252C885.635 84.0484 885.238 83.5923 884.786 83.6518L883.792 83.7444L882.234 84.1052C881.607 84.2569 881.17 83.4506 881.639 83.0093L882.791 81.9003L883.41 81.1164C883.72 80.7244 883.51 80.1303 883.039 80.0875L880.425 79.6027C880.425 79.6027 880.038 79.4398 879.958 79.2224L873.701 64.5992C873.589 64.3236 873.681 64.0127 873.925 63.8432L878.019 60.8005C878.32 60.5993 878.733 60.6738 878.947 60.9304L889.386 75.1491C889.588 75.4512 890.013 75.4801 890.316 75.2804L898.949 68.5046C899.193 68.3352 899.241 68.0116 899.174 67.7499L877.491 13.15C877.379 12.8758 877.484 12.5192 877.728 12.3496L886.172 7.35653C886.475 7.1567 886.875 7.27552 887.062 7.62048C896.16 23.4247 914.121 54.5278 915.599 57.0456C917.015 59.4483 919.263 58.2291 920.373 57.2515C920.503 57.1453 920.541 57.0113 920.55 56.8204L920.681 54.5867C920.681 54.5867 920.799 54.1859 920.972 54.0923C924.337 52.0434 926.98 50.795 929.163 50.2811C929.731 50.1596 929.968 49.3593 929.487 49.0232L925.855 46.1091C925.582 45.8829 925.542 45.5327 925.722 45.2469L927.12 43.1468C927.372 42.7865 927.868 42.7395 928.159 43.0682L935.942 52.0489C935.942 52.0489 936.031 52.0755 936.076 52.0895C937.11 51.8642 938.141 51.9764 938.61 52.8409C938.891 53.3591 938.835 53.8748 938.543 54.3679C938.393 54.7105 938.422 55.1062 938.693 55.3312L946.927 61.9808C947.198 62.2058 947.24 62.5571 947.059 62.8416L945.662 64.9431L945.639 64.6941Z" fill="white" fill-opacity="0.36"/>'
 '</g></svg>')

for page in ('tri-stihii-urala.html', 'index.html'):
    p = os.path.join(ROOT, page); s = open(p, encoding='utf-8').read()
    s = s.replace('assets/video/hero-taiga.mp4', 'assets/video/hero-summer.mp4').replace('assets/img/hero-taiga.webp', 'assets/img/hero-summer.webp')
    if page == 'tri-stihii-urala.html':
        s = s.replace('<h1>Три стихии Урала</h1>', '<h1>Три стихии<br><span class="h1-big">Урала</span></h1>')
        if 'exp-decor' not in s:
            s = s.replace('<section class="expect" id="expect">', '<section class="expect" id="expect">' + DECOR, 1)
        s = re.sub(r'\s*<svg class="facts-path".*?</svg>', '', s, flags=re.S)
        s = re.sub(r'\s*<svg class="facts-plane".*?</svg>', '', s, flags=re.S)
    open(p, 'w', encoding='utf-8').write(s)

header = f'''
/* ===== Frame 2 v3: header — nav left, logo centre, contacts right ===== */
.head-in{{display:grid!important;grid-template-columns:1fr auto 1fr;padding:0 {v(63,16)} 0 {v(62,16)}!important}}
.head-in>.brand{{grid-column:2;grid-row:1;justify-self:center}}
.head-in>nav{{grid-column:1;grid-row:1;justify-self:start;margin-left:0!important}}
.head-in>.head-cta{{grid-column:3;grid-row:1;justify-self:end;margin-left:0!important}}
@media (max-width:900px){{.head-in{{grid-template-columns:auto 1fr}}.head-in>.brand{{grid-column:1;justify-self:start}}.head-in>.head-cta{{grid-column:2}}}}
'''
tour = header + f'''
/* ===== Frame 2 v3: hero ===== */
.hero-f2 .hero-main{{padding-top:{v(172,110)}!important}}
.hero-f2 h1{{font-size:{v(98,40)}!important;line-height:.92!important;white-space:normal!important}}
.hero-f2 h1 .h1-big{{display:block;font-size:{v(158,64)};line-height:.92;text-transform:uppercase}}
.hero-f2 .hero-desc{{font-size:{v(21,15)}!important;line-height:1.2!important;max-width:{v(469,280)}!important;margin-top:{v(21,14)}!important}}
.hero-f2 .hero-links{{margin-top:{v(47,26)}!important}}

/* ===== Frame 2 v3: expect ===== */
main>section.expect#expect{{padding-top:{v(76,44)}!important;position:relative;background:
  radial-gradient(60% 16% at 50% 62%,rgba(0,155,248,.5),rgba(0,155,248,0) 70%),
  linear-gradient(180deg,#0A2A6B 0%,#003DB0 5%,#0040B5 44%,#0052C3 54%,#0079E9 62%,#009BF8 72%,#009BF8 100%)!important}}
.exp-decor{{position:absolute;left:{v(423)};top:{v(72)};width:{v(978)};height:auto;pointer-events:none;z-index:0}}
.expect>.wrap{{position:relative;z-index:1}}
.fan{{margin-top:{v(62,28)}!important;gap:{v(15,12)}!important}}
.fan-card{{width:{v(367,220)}!important;aspect-ratio:367/495!important}}
.fan-card.c1,.fan-card.c3{{margin-top:0!important}}
.fan-card.c2{{margin-top:{v(36,0)}!important}}
.exp-lead{{margin-top:{v(65,32)}!important}}
.facts{{margin-top:{v(65,36)}!important;padding-bottom:{v(130,56)}!important}}
.facts-path,.facts-plane{{display:none!important}}
main>section#route{{padding-top:{v(140,48)}!important}}
@media (max-width:900px){{.exp-decor{{display:none}}}}
'''
open(os.path.join(ROOT, 'assets', 'css', 'tour.css'), 'a', encoding='utf-8').write(tour)
open(os.path.join(ROOT, 'assets', 'css', 'home.css'), 'a', encoding='utf-8').write(header)
print('ok')
