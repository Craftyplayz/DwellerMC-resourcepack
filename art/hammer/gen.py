# Hammer (3x3 mining hammer) item icon. Run: py gen.py -> ../../assets/dwellermc/textures/item/hammer.png + preview.png (12x)
from PIL import Image

T = (0, 0, 0, 0)
K = (0x14, 0x12, 0x18, 255)
C = {
    "d": (0x2e, 0x2c, 0x34, 255), "m": (0x4c, 0x48, 0x55, 255), "l": (0x7a, 0x74, 0x86, 255),
    "h": (0xb4, 0xae, 0xc4, 255), "q": (0x4a, 0x3a, 0x28, 255), "r": (0x6b, 0x54, 0x38, 255), "R": (0x8a, 0x6f, 0x4a, 255),
}
G = [
    "................",
    "...hllllllllll..",
    "..hlmmmmmmmmmmd.",
    "..lmmddddddmmmd.",
    "..lmmdmmmmdmmmd.",
    "..lmmddddddmmmd.",
    "..lmmmmmmmmmmdd.",
    "...dddddddddd...",
    "................",
    "................",
] + ["................"] * 6
img = Image.new("RGBA", (16, 16), T)
p = img.load()
for y, row in enumerate(G):
    for x, c in enumerate(row):
        if c != ".":
            p[x, y] = C[c]
for i in range(8):  # handle runs from under the head to the bottom-left
    p[9 - i, 8 + i] = C["R"]
    p[10 - i, 8 + i] = C["q"]
filled = {(x, y) for y in range(16) for x in range(16) if p[x, y][3]}
for y in range(16):
    for x in range(16):
        if (x, y) not in filled and any((x + a, y + b) in filled for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            p[x, y] = K
img.save("../../assets/dwellermc/textures/item/hammer.png")
bg = Image.new("RGBA", (192, 192), (0x8b, 0x8b, 0x8b, 255))
bg.alpha_composite(img.resize((192, 192), Image.NEAREST))
bg.convert("RGB").save("preview.png")
