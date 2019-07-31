#!/usr/bin/env python2

# only works for rar5 format

import sys

def ReadVint(myba, start):
	'''
	Read and return "vint" from myba (my byte array), starting at start
	Definition of vint: https://www.rarlab.com/technote.htm#vint
	Example:
	63 (0b) means 100: 0x63 = 99, plus 1, makes 100. Highest bit of 0x63 is not set ('0'), so stop
	f0 03 means 497: f0 => (7 lowest bits) 0x70 = 112. Highest bit set, so continue. 03 = 0x03 * 128, makes 384. Total 112 + 3 * 128 + 1 = 497
	'''

	i = start
	result = 1 # yes, start at 1 (because volume #1 will have '0')
	weight = 1 # we start at weight 1 for the first 'septet' (7-bit byte), and mutiply with 128 (not 256)

	while True:
		if ba[i]<128:
			# most significant bit NOT set, so last entry
			result += weight * ba[i]
			break	# done
		else:
			# most signifcant bit is set, so we'll have to continu
			result += weight * (ba[i]-128)
			weight *= 128
			i += 1
	return result

fh = open(sys.argv[1])
ba = bytearray(fh.read())
if ba[0:4] != 'Rar!':
	# RAR 5.0 signature consists of 8 bytes: 0x52 0x61 0x72 0x21 0x1A 0x07 0x01 0x00
	print "Not a rar file!!!"
	sys.exit(-1)

i=17 # reverse engineering, only works if there is one file in this rar file ...
print "Volume Number result is", ReadVint(ba,i)


low = high = 0
x = 12 - 1 	# skip "Rar! ..." (8 bytes) and CRC (4 bytes)
while x<17:
	if ba[x] < 128:
		low +=1
	else:
		high += 1
	x += 1

print "low", low, "high", high


