#!/usr/bin/env python2

# only works for rar3 / rar4 format

# Hacked together based on reverse engineering with hd and diff

import sys

'''

$ hd rar4.part490.rar | tail -2
000ffff0  40 14 00 25 9e f8 19 e9  01 00 00 00 00 00 00 00  |@..%............|
00100000

We want the e9 01 => 0x01e9 = 489, plus 1, gives 490.


$ hd some-rar4-file-eightyeight-blabla | tail -2
000ffff0  40 14 00 53 a8 4a b5 57  00 00 00 00 00 00 00 00  |@..S.J.W........|
00100000

We want the 57 00 => 0x0057 = 87, plus 1, gives 88

'''

# Open file passed as argument, and put into a bytearray
fh = open(sys.argv[1],"rb")
ba = bytearray(fh.read())

#print len(ba)

pos = len(ba)
'''
i=1
while i<20: 
	print i, ba[pos-i]
	i += 1
'''

print 1 + ba[pos-9] + 256 * ba[pos-8] 
