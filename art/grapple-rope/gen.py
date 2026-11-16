import random
from PIL import Image
random.seed(7)
K=(0x3a,0x32,0x29,255); D=(0x58,0x4e,0x40,255); M=(0x7b,0x6f,0x5b,255); L=(0xa0,0x94,0x7c,255); H=(0xc2,0xb8,0x9f,255)
T=(0,0,0,0)
img=Image.new("RGBA",(16,16),T); p=img.load()
# strand: x 6..9, diagonal twist, period 4 rows (divides 16 -> seamless)
tw=[L,M,M,D]
for y in range(16):
    for x in range(6,10):
        c=tw[(y+x)%4]
        if x==6 and c in(M,D): c=L if c==M else M   # light from left
        if x==9: c=D if c!=D else K                   # shaded right edge
        p[x,y]=c
# knot rows 5..10
rows={5:(5,10),6:(4,11),7:(4,11),8:(4,11),9:(4,11),10:(5,10)}
for y,(a,b) in rows.items():
    for x in range(a,b+1):
        edge=x in(a,b) or y in(5,10)
        c=M
        if x<=a+1 and y<=7: c=L
        if x>=b-1 or y>=10: c=D
        if (x+y)%4==0 and a<x<b and 5<y<10: c=D if c!=D else K  # wrap lines
        if y==6 and x in(a+1,a+2): c=H
        if edge: c=K if (x>=b or y==10) else D
        p[x,y]=c
img.save("rope.png")
# tile3
t=Image.new("RGBA",(16,48))
for i in range(3): t.paste(img,(0,16*i))
bg=Image.new("RGBA",(16*8+64,48*8+64),(110,110,110,255))
bg.alpha_composite(t.resize((128,384),Image.NEAREST),(32,32)); bg.save("tile3.png")
# preview
def tile(base,var):
    t=Image.new("RGBA",(16,16)); q=t.load()
    for y in range(16):
        for x in range(16):
            v=base+random.randint(-var,var)
            q[x,y]=(v,v,v+4,255)
    for _ in range(6):
        x,y=random.randrange(14),random.randrange(14); v=base-14
        for dx,dy in((0,0),(1,0),(0,1)): q[x+dx,y+dy]=(v,v,v+4,255)
    return t
tiles=[tile(52,5) for _ in range(6)]; stone=[tile(78,6) for _ in range(4)]
S=Image.new("RGBA",(160,160))
for by in range(10):
    for bx in range(10):
        S.paste(random.choice(tiles),(bx*16,by*16))
for by in(0,1):
    for bx in range(5): S.paste(random.choice(stone),(bx*16,by*16))
for bx in range(10): S.paste(random.choice(stone),(bx*16,144))
rp=img.load(); sp=S.load()
for by in range(2,9):
    for y in range(16):
        for x in range(16):
            c=rp[x,y]
            if c[3]: sp[5*0+ 64+x,by*16+y]=tuple(int(v*0.9) for v in c[:3])+(255,)
            # crossed plane edge-on sliver
            if x==7 and c[3]: sp[64+8,by*16+y]=tuple(int(v*0.7) for v in c[:3])+(255,)
# player 2 blocks tall (32px) at x 90..105 standing on floor (y 144)
sk=(176,128,96,255); sh=(60,160,170,255); pt=(60,60,150,255)
def r(x0,y0,x1,y1,c):
    for y in range(y0,y1):
        for x in range(x0,x1): sp[x,y]=c
r(94,112,102,120,sk); r(94,112,102,114,(70,50,35,255))   # head
r(94,120,102,132,sh); r(90,120,94,132,sh); r(102,120,106,132,sh)
r(94,132,98,144,pt); r(98,132,102,144,pt)
d=Image.new("RGBA",(160,160),(0,0,0,70)); S.alpha_composite(d)
S.convert("RGB").resize((640,640),Image.NEAREST).save("preview.png")
