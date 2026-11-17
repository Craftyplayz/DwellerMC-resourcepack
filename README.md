# DwellerMC resource pack

The server resource pack for DwellerMC. Players get it automatically when they join; it is required.

Every push to `main` zips the pack and uploads it to the `pack` release:

- Pack: https://github.com/Craftyplayz/DwellerMC-resourcepack/releases/download/pack/DwellerMC.zip
- SHA-1: https://github.com/Craftyplayz/DwellerMC-resourcepack/releases/download/pack/DwellerMC.zip.sha1

DwellerCore downloads the SHA-1 when the server starts, so after a pack change a server restart is enough.

## Contents

| File | Used by |
|---|---|
| `assets/dwellermc/items/grappling_hook.json` | DwellerTools Grappling Hook item (`item_model`) |
| `assets/dwellermc/items/rope.json` | DwellerTools rope blocks (item displays) |
| `assets/dwellermc/items/drill.json` | DwellerTools Drill item (`item_model`) |
| `assets/dwellermc/items/hammer.json` | DwellerTools Hammer item (`item_model`) |
| `assets/dwellermc/items/paxel.json` | DwellerTools Paxel item (`item_model`) |
| `assets/minecraft/sounds.json` | DwellerEnchants: silences the totem sound (the attune animation is a silent totem; real totems are silent too) |

## Textures

The DwellerTools items use vanilla models as placeholders until the owner's art is added (grappling hook: tripwire hook, drill and hammer: netherite pickaxe, paxel: netherite axe, rope: chain). To add art, drop the PNG in `assets/dwellermc/textures/item/<name>.png` (`grappling_hook`, `drill`, `hammer`, `paxel`; the rope uses `assets/dwellermc/textures/block/rope.png`), add a model in `assets/dwellermc/models/item/<name>.json` (`minecraft:item/generated` with `layer0` pointing at the texture), and point `assets/dwellermc/items/<name>.json` at it. Keep the item definition files: the plugins reference these ids.

Pack format 97 (Minecraft 26.3).
