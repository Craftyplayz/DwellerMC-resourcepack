# Grapple item icon options. Run: py gen.py -> icon_<n>.png (16x16) + options.png (preview sheet)
import math
from PIL import Image, ImageDraw

T = (0, 0, 0, 0)
K = (0x1e, 0x1e, 0x22, 255)
ROPE = {"q": (0x58, 0x4e, 0x40, 255), "r": (0x7b, 0x6f, 0x5b, 255), "R": (0xa0, 0x94, 0x7c, 255)}
METALS = {
    "iron":   {"d": (0x5a, 0x5a, 0x60, 255), "m": (0x9a, 0x9a, 0xa0, 255), "l": (0xd8, 0xd8, 0xdc, 255)},
    "dark":   {"d": (0x2e, 0x2c, 0x34, 255), "m": (0x4c, 0x48, 0x55, 255), "l": (0x7a, 0x74, 0x86, 255)},
    "copper": {"d": (0x8a, 0x45, 0x2c, 255), "m": (0xc0, 0x6b, 0x4b, 255), "l": (0xe8, 0x9c, 0x74, 255)},
}

ANCHOR = [
    "................",
    "......kkkk......",
    ".....kl..dk.....",
    ".....kl..dk.....",
    "......kkkk......",
    "......klmk......",
    "......klmk......",
    "....kkklmkkk....",
    "....kllllmmk....",
    "....kkklmkkk....",
    ".kk...klmk...kk.",
    "kllk..klmk..kmdk",
    ".klmk.klmk.kmdk.",
    "..klmkklmkkmdk..",
    "...kllllmmmmk...",
    "....kkkkkkkk....",
]
HANGING = [
    "....kkkkkkkk....",
    "...klllllmmmk...",
    "..klmkklmkkmdk..",
    ".klmk.klmk.kmdk.",
    "kllk..klmk..kmdk",
    ".kk...klmk...kk.",
    "......klmk......",
    "......kkkk......",
    "......kRrk......",
    ".......kRrk.....",
    ".......kRrk.....",
    "......kRrk......",
    "......kRrk......",
    ".......kRrk.....",
    ".......kRrk.....",
    "........kk......",
]
# fill-only grids: outline added automatically
JHOOK = [
    "................",
    "............lm..",
    "............lm..",
    "............lm..",
    ".........l..lm..",
    ".........lllmd..",
] + ["................"] * 10
PICK = [
    "................",
    "................",
    "................",
    "........lllll...",
    ".......lmmmmmd..",
    "......lm..rRd...",
    "......m..rRq....",
    "........rRq.....",
    ".......rRq......",
    "......rRq.......",
    ".....rRq........",
    "....rRq.........",
    "...rRq..........",
    "..lmd...........",
    "................",
    "................",
]


def draw(grid, metal, outline=False, coil=False):
    pal = {"k": K, **ROPE, **METALS[metal]}
    img = Image.new("RGBA", (16, 16), T)
    p = img.load()
    if coil:
        for y in range(16):
            for x in range(16):
                d = math.hypot(x - 5.5, y - 9.5)
                if 2.6 <= d <= 5.0:
                    a = int((math.atan2(y - 9.5, x - 5.5) + math.pi) / (2 * math.pi) * 12)
                    p[x, y] = ROPE["Rrq"[a % 3]] if d < 4.2 else ROPE["q"]
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != ".":
                p[x, y] = pal[c]
    if outline:
        filled = {(x, y) for y in range(16) for x in range(16) if p[x, y][3]}
        for x, y in [(x, y) for y in range(16) for x in range(16)]:
            if (x, y) not in filled and any((x + dx, y + dy) in filled for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                p[x, y] = K
    return img


OPTIONS = [
    ("1 Anchor", draw(ANCHOR, "iron")),
    ("2 Hanging grapple", draw(HANGING, "iron")),
    ("3 Hook + coil", draw(JHOOK, "iron", outline=True, coil=True)),
    ("4 Climbing pick", draw(PICK, "iron", outline=True)),
    ("5 Hanging, blackened", draw(HANGING, "dark")),
    ("6 Hanging, copper", draw(HANGING, "copper")),
]

S, PAD = 12, 24
sheet = Image.new("RGBA", (len(OPTIONS) * (16 * S + PAD) + PAD, 16 * S + 110), (0x30, 0x30, 0x34, 255))
d = ImageDraw.Draw(sheet)
for i, (name, icon) in enumerate(OPTIONS):
    icon.save(f"icon_{i + 1}.png")
    x = PAD + i * (16 * S + PAD)
    sheet.alpha_composite(Image.new("RGBA", (16 * S, 16 * S), (0x8b, 0x8b, 0x8b, 255)), (x, PAD))
    sheet.alpha_composite(icon.resize((16 * S, 16 * S), Image.NEAREST), (x, PAD))
    slot = Image.new("RGBA", (36, 36), (0x8b, 0x8b, 0x8b, 255))  # inventory slot at GUI scale 2
    slot.alpha_composite(icon.resize((32, 32), Image.NEAREST), (2, 2))
    sheet.alpha_composite(slot, (x, PAD + 16 * S + 12))
    d.text((x + 48, PAD + 16 * S + 24), name, fill=(240, 240, 240, 255))
sheet.convert("RGB").save("options.png")
