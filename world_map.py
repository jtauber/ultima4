from png import write_png

from shapes import load_shapes


SHAPES = load_shapes()


world = open("ULT/WORLD.MAP").read()
pixels = []
for chunk_row in range(8):
    for row in range(32):
        for shape_row in range(16):
            for chunk_col in range(8):
                for col in range(32):
                    for shape_col in range(16):
                        world_offset = (8 * chunk_row + chunk_col) * 1024 + (32 * row + col)
                        pixels.append(SHAPES[ord(world[world_offset])][16 * shape_row + shape_col])

write_png("world.png", 4096, 4096, pixels)
