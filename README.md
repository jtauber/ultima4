ultima4
=======

code for exploring Ultima IV data files


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
