#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print "usage: {} <TLK FILE>".format(sys.argv[0])
else:
    with open(sys.argv[1]) as talk_file:
        talk_data = talk_file.read()

        KEY = ["Name", "Pronoun", "Look", "Job", "Health", "Keyword 1", "Keyword 2",
            "Question", "Yes", "No"]

        for char in range(16):
            char_data = talk_data[0x120 * char:0x120 * (char + 1)]

            print "\ncharacter %d" % char
            print ord(char_data[0]), ord(char_data[1]), ord(char_data[2])

            start = 0x3
            for i in range(10):
                length = char_data[start:].find("\0")
                print KEY[i], repr(char_data[start:start + length])
                start += length + 1
