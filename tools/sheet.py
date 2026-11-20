import sys, os
from PIL import Image
shots, out = sys.argv[1], sys.argv[2]
names = sorted({f.split('__')[0] for f in os.listdir(shots) if f.endswith('.png')})
for n in names:
    ims = []
    for c in ['phone-light','phone-dark','desktop-light','desktop-dark']:
        p = os.path.join(shots, f'{n}__{c}.png')
        im = Image.open(p).convert('RGB')
        tw = 390 if c.startswith('phone') else 700
        im = im.resize((tw, int(im.height*tw/im.width)))
        im = im.crop((0,0,tw,min(im.height, 2200 if c.startswith('phone') else 1300)))
        ims.append(im)
    W = sum(i.width for i in ims) + 10*3; H = max(i.height for i in ims)
    sh = Image.new('RGB',(W,H),(128,128,128)); x=0
    for i in ims: sh.paste(i,(x,0)); x+=i.width+10
    sh.save(os.path.join(out, n+'.png'))
print(len(names))
