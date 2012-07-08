from png import write_png


EGA2RGB = [
    (0x00, 0x00, 0x00),
    (0x00, 0x00, 0xAA),
    (0x00, 0xAA, 0x00),
    (0x00, 0xAA, 0xAA),
    (0xAA, 0x00, 0x00),
    (0xAA, 0x00, 0xAA),
    (0xAA, 0x55, 0x00),
    (0xAA, 0xAA, 0xAA),
    (0x55, 0x55, 0x55),
    (0x55, 0x55, 0xFF),
    (0x55, 0xFF, 0x55),
    (0x55, 0xFF, 0xFF),
    (0xFF, 0x55, 0x55),
    (0xFF, 0x55, 0xFF),
    (0xFF, 0xFF, 0x55),
    (0xFF, 0xFF, 0xFF),
]


def rle(filename_in, filename_out, w, h):
    pixels = []
    bytes = open(filename_in).read()
    
    state = 0
    for d in map(ord, bytes):
        if state == 0:
            if d == 0x02:
                state = 1
            else:
                a, b = divmod(d, 16)
                pixels.append(EGA2RGB[a])
                pixels.append(EGA2RGB[b])
        elif state == 1:
            run = d
            state = 2
        elif state == 2:
            for i in range(run):
                a, b = divmod(d, 16)
                pixels.append(EGA2RGB[a])
                pixels.append(EGA2RGB[b])
            state = 0
    
    write_png(filename_out, w, h, pixels)


rle("EGA/START.EGA", "start.png", 320, 200)
rle("EGA/KEY7.EGA", "key7.png", 320, 200)
rle("EGA/RUNE_0.EGA", "rune_0.png", 320, 200)
rle("EGA/RUNE_1.EGA", "rune_1.png", 320, 200)
rle("EGA/RUNE_2.EGA", "rune_2.png", 320, 200)
rle("EGA/RUNE_3.EGA", "rune_3.png", 320, 200)
rle("EGA/RUNE_4.EGA", "rune_4.png", 320, 200)
rle("EGA/RUNE_5.EGA", "rune_5.png", 320, 200)
rle("EGA/STONCRCL.EGA", "stonecircle.png", 320, 200)
rle("EGA/HONESTY.EGA", "honesty.png", 320, 200)
rle("EGA/COMPASSN.EGA", "compassion.png", 320, 200)
rle("EGA/VALOR.EGA", "valor.png", 320, 200)
rle("EGA/JUSTICE.EGA", "justice.png", 320, 200)
rle("EGA/SACRIFIC.EGA", "sacrifice.png", 320, 200)
rle("EGA/HONOR.EGA", "honor.png", 320, 200)
rle("EGA/SPIRIT.EGA", "spirit.png", 320, 200)
rle("EGA/HUMILITY.EGA", "humility.png", 320, 200)
rle("EGA/TRUTH.EGA", "truth.png", 320, 200)
rle("EGA/LOVE.EGA", "love.png", 320, 200)
rle("EGA/COURAGE.EGA", "courage.png", 320, 200)
