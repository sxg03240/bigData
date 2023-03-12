#!/usr/bin/env python3
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    #clean and split in words
    line = line.strip()
    words = line.split()

    #emit the key-balue pairs
    for word in words:
        print ('{}\t{}'.format(word, 1))
