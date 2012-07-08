import zlib
import struct
import array


def output_chunk(out, chunk_type, data):
    out.write(struct.pack("!I", len(data)))
    out.write(chunk_type)
    out.write(data)
    checksum = zlib.crc32(data, zlib.crc32(chunk_type))
    out.write(struct.pack("!i", checksum))


def get_data(width, height, pixels):
    compressor = zlib.compressobj()
    data = array.array("B")
    for y in range(height):
        data.append(0)
        for x in range(width):
            data.extend(pixels[y * width + x])
    compressed = compressor.compress(data.tostring())
    flushed = compressor.flush()
    return compressed + flushed


def write_png(filename, width, height, pixels):
    out = open(filename, "w")
    out.write(struct.pack("8B", 137, 80, 78, 71, 13, 10, 26, 10))
    output_chunk(out, "IHDR", struct.pack("!2I5B", width, height, 8, 2, 0, 0, 0))
    output_chunk(out, "IDAT", get_data(width, height, pixels))
    output_chunk(out, "IEND", "")
    out.close()


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


shapes = []
bytes = open("EGA/SHAPES.EGA").read()

for i in range(256):
    shape = []
    for j in range(16):
        for k in range(8):
            d = ord(bytes[k + 8 * j + 128 * i])
            a, b = divmod(d, 16)
            shape.append(EGA2RGB[a])
            shape.append(EGA2RGB[b])
    shapes.append(shape)


world = open("WORLD.MAP").read()
pixels = []
for chunk_row in range(8):
    for row in range(32):
        for shape_row in range(16):
            for chunk_col in range(8):
                for col in range(32):
                    for shape_col in range(16):
                        world_offset = (8 * chunk_row + chunk_col) * 1024 + (32 * row + col)
                        pixels.append(shapes[ord(world[world_offset])][16 * shape_row + shape_col])

write_png("world.png", 4096, 4096, pixels)
