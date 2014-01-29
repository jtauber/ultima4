ultima4
=======

code for exploring Ultima IV data files

The output of `world_map.py` is available at https://raw.github.com/jtauber/ultima4/master/world.png (also included in repo)

If you get Ultima IV for OS X from GOG.com, the relevant files are in `Ultima 4.app/Contents/Resources/Ultima IV- Quest of the Avatar.boxer/C.harddisk` which you can symlink `ULT` to for the scripts here to work.

png.py
------
module for writing images out as PNG files

ega.py
------
script for outputting the RLE-encoding `.EGA` files as PNGs

shapes.py
---------
module for reading `SHAPES.EGA` file (used by `world_map.py` and `town_maps.py`)

world_map.py
------------
script that reads `WORLD.MAP` and generates a PNG world map

town_maps.py
------------
script that extracts the maps out of the various town `.ULT` files and generates a PNG of each map

town_data.py (in progress)
--------------------------
work in progress understanding the rest of the town data (i.e. non-map) in `.ULT` files

town_talk.py (in progress)
--------------------------
work in progress understanding the `.TLK` files
