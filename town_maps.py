from png import write_png

from shapes import load_shapes


SHAPES = load_shapes()


def town_map(filename_in, filename_out):
    t_map = open(filename_in).read(1024)
    pixels = []
    for row in range(32):
        for shape_row in range(16):
            for col in range(32):
                for shape_col in range(16):
                    town_offset = 32 * row + col
                    pixels.append(SHAPES[ord(t_map[town_offset])][16 * shape_row + shape_col])
    write_png(filename_out, 512, 512, pixels)


town_map("ULT/BRITAIN.ULT", "britain.png")
town_map("ULT/COVE.ULT", "cove.png")
town_map("ULT/DEN.ULT", "den.png")
town_map("ULT/EMPATH.ULT", "empath.png")
town_map("ULT/JHELOM.ULT", "jhelom.png")
town_map("ULT/LCB_1.ULT", "lcb_1.png")
town_map("ULT/LCB_2.ULT", "lcb_2.png")
town_map("ULT/LYCAEUM.ULT", "lycaeum.png")
town_map("ULT/MAGINCIA.ULT", "magincia.png")
town_map("ULT/MINOC.ULT", "minoc.png")
town_map("ULT/MOONGLOW.ULT", "moonglow.png")
town_map("ULT/PAWS.ULT", "paws.png")
town_map("ULT/SERPENT.ULT", "serpent.png")
town_map("ULT/SKARA.ULT", "skara.png")
town_map("ULT/TRINSIC.ULT", "trinsic.png")
town_map("ULT/VESPER.ULT", "vesper.png")
town_map("ULT/YEW.ULT", "yew.png")
