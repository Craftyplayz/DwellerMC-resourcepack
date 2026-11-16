# Paxel (pickaxe + axe + shovel) item icon. Run: py gen.py -> ../../assets/dwellermc/textures/item/paxel.png + preview.png (12x)
from PIL import Image

T = (0, 0, 0, 0)
K = (0x14, 0x12, 0x18, 255)
C = {
    "d": (0x2e, 0x2c, 0x34, 255), "m": (0x4c, 0x48, 0x55, 255), "l": (0x7a, 0x74, 0x86, 255),
    "h": (0xb4, 0xae, 0xc4, 255), "q": (0x4a, 0x3a, 0x28, 255), "r": (0x6b, 0x54, 0x38, 255), "R": (0x8a, 0x6f, 0x4a, 255),
}
def cell(t, u):
    # t runs along the handle toward the tip, u across it (pickaxe side negative, axe side positive)
    if -15 <= t <= 7 and abs(u) <= 1 and not (abs(u) == 1 and t < -13):
        return "R" if u < 0 else ("r" if u == 0 else "q")  # handle
    if 6 <= t <= 13 and abs(u) <= {6: 3, 7: 3, 8: 3, 9: 3, 10: 3, 11: 2, 12: 1, 13: 0}[t]:
        return "h" if u < 0 and t > 8 else ("l" if u <= 0 else ("m" if u < 3 else "d"))  # shovel spade
    if t in (1, 2) and -8 <= u <= -2 or (t in (-1, 0) and u in (-8, -7)):
        return "h" if t == 2 else ("l" if u < -4 else "m")  # pickaxe bar with drooping tip
    if 2 <= u <= 7 and abs(t - 1) <= {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3}[u]:
        return "l" if u == 7 or t == 4 else ("m" if u > 4 else "d")  # axe blade
    return None


img = Image.new("RGBA", (16, 16), T)
p = img.load()
for y in range(16):
    for x in range(16):
        c = cell(x - y, x + y - 15)
        if c:
            p[x, y] = C[c]
filled = {(x, y) for y in range(16) for x in range(16) if p[x, y][3]}
for y in range(16):
    for x in range(16):
        if (x, y) not in filled and any((x + a, y + b) in filled for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            p[x, y] = K
img.save("../../assets/dwellermc/textures/item/paxel.png")
bg = Image.new("RGBA", (192, 192), (0x8b, 0x8b, 0x8b, 255))
bg.alpha_composite(img.resize((192, 192), Image.NEAREST))
bg.convert("RGB").save("preview.png")
