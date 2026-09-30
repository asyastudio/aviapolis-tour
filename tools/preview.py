"""Собирает страницу в один файл для просмотра (все стили, скрипты, фото и шрифты внутри).
Запуск: python tools/preview.py tri-stihii-urala.html preview/tri-stihii-urala.html"""
import base64,os,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src,out=sys.argv[1],sys.argv[2]
MT={'svg':'image/svg+xml','webp':'image/webp','png':'image/png','jpg':'image/jpeg','woff2':'font/woff2'}
def data(path):
    ext=path.rsplit('.',1)[1]
    return f'data:{MT[ext]};base64,'+base64.b64encode(open(os.path.join(ROOT,path),'rb').read()).decode()
h=open(os.path.join(ROOT,src),encoding='utf-8').read()
def css(m):
    c=open(os.path.join(ROOT,m.group(1)),encoding='utf-8').read()
    c=re.sub(r'\.\./(img|fonts)/([\w.-]+)',lambda x:data(f'assets/{x.group(1)}/{x.group(2)}'),c)
    return '<style>'+c+'</style>'
h=re.sub(r'<link rel="stylesheet" href="(assets/css/[\w.-]+)">',css,h)
h=re.sub(r'<script src="(assets/js/[\w.-]+)" defer></script>',lambda m:'<script>'+open(os.path.join(ROOT,m.group(1)),encoding='utf-8').read()+'</script>',h)
h=re.sub(r'assets/img/[\w.-]+\.(?:webp|png|jpg|svg)',lambda m:data(m.group(0)),h)
os.makedirs(os.path.dirname(os.path.join(ROOT,out)),exist_ok=True)
open(os.path.join(ROOT,out),'w',encoding='utf-8').write(h)
print(len(h)//1024,'KB')
