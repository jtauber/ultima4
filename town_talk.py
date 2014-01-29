#!/usr/bin/env python

import sys

TALK_TEMPLATE = """
NAME: {0} ({1})
LOOK: {2}
JOB : {3}
HEAL: {4}
{10}: {5}
{11}: {6}

{7}
YES : {8}
NO  : {9}
"""

if len(sys.argv) != 2:
    print "usage: {} <TLK FILE>".format(sys.argv[0])
else:
    with open(sys.argv[1]) as talk_file:
        talk_data = talk_file.read()

        for char in range(16):
            char_data = talk_data[0x120 * char:0x120 * (char + 1)]

            slot = [None] * 12
            start = 0x3
            for i in range(12):
                length = char_data[start:].find("\0")
                slot[i] = char_data[start:start + length].replace("\n", " ")
                start += length + 1

            print "\ncharacter %d" % char
            print ord(char_data[0]), ord(char_data[1]), ord(char_data[2])

            print TALK_TEMPLATE.format(*slot)
