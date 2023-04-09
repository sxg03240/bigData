#!/usr/bin/env python3
import sys

"""Group - 5
Sai Surekha Gandu(700740324)
Mallory Sims (700698245)
Keerthi Sreelekha (700739980)
Maheshwar Reddy Upputuri (700741748)
Jitheandra Subramaniam (700742721)
"""

# input comes from STDIN (standard input)
for line in sys.stdin:
    #clean and split in words
    line = line.strip()
    words = line.split()

    #emit the key-balue pairs
    for word in words:
        print ('{}\t{}'.format(word, 1))
