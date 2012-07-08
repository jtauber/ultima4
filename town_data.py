town = open("ULT/BRITAIN.ULT").read()

for char in range(32):
    tile1, x_pos1, y_pos1, tile2, x_pos2, y_pos2, move, char_id = [ord(town[1024 + (32 * i) + char]) for i in range(8)]
    print "%s: %s %s/%s (%s, %s) (%s, %s) %s" % (char, char_id, tile1, tile2, x_pos1, y_pos1, x_pos2, y_pos2, move)
