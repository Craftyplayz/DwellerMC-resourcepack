# Drill item icon. Run: py gen.py -> ../../assets/dwellermc/textures/item/drill.png + preview.png (12x)
from PIL import Image

T = (0, 0, 0, 0)
K = (0x14, 0x12, 0x18, 255)
C = {
    "d": (0x2e, 0x2c, 0x34, 255), "m": (0x4c, 0x48, 0x55, 255), "l": (0x7a, 0x74, 0x86, 255),
    "q": (0x4a, 0x3a, 0x28, 255), "r": (0x6b, 0x54, 0x38, 255), "R": (0x8a, 0x6f, 0x4a, 255),
    "o": (0xe0, 0x7a, 0x1e, 255), "g": (0xf2, 0xc2, 0x3c, 255), "h": (0xb4, 0xae, 0xc4, 255),
}
img = Image.new("RGBA", (16, 16), T)
p = img.load()
for y in range(16):
    for x in range(16):
        t, u = x - y, x + y - 15  # t along the tool (tip at 13), u across it
        c = None
        if 4 <= t <= 13 and abs(u) <= round((14 - t) * 0.4):  # conical bit
            c = ("h" if u <= 0 else "l") if ((t + 1) // 2) % 2 else ("m" if u <= 0 else "d")  # spiral flutes
        elif 1 <= t <= 3 and abs(u) <= 3:  # gold chuck
            c = "g" if u <= 0 else "o"
        elif -5 <= t <= 0 and abs(u) <= 3:  # motor
            c = "l" if u <= -2 else ("m" if u <= 1 else "d")
            if t in (-2, -3) and abs(u) <= 1: c = "o"  # powered accent
        elif -11 <= t <= -6 and abs(u) <= 1:  # handle
            c = "R" if u < 0 else ("r" if u == 0 else "q")
        if c:
            p[x, y] = C[c]
filled = {(x, y) for y in range(16) for x in range(16) if p[x, y][3]}
for y in range(16):
    for x in range(16):
        if (x, y) not in filled and any((x + a, y + b) in filled for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            p[x, y] = K
img.save("../../assets/dwellermc/textures/item/drill.png")
bg = Image.new("RGBA", (192, 192), (0x8b, 0x8b, 0x8b, 255))
bg.alpha_composite(img.resize((192, 192), Image.NEAREST))
bg.convert("RGB").save("preview.png")
