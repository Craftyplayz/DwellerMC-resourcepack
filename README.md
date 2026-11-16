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

`art/` holds the scripts that draw the textures (`py gen.py` in each folder). Copy a chosen result into `assets/`.

Pack format 97 (Minecraft 26.3).
