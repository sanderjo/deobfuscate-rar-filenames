#!/usr/bin/env python2

# only works for rar5 format

import sys

'''
Definition of vint: https://www.rarlab.com/technote.htm#vint
Examples:

63 (0b) means 100: 0x63 = 99, plus 1, makes 100. Highest bit of 0x63 is not set ('0'), so stop

f0 03 means 497: f0 => (7 lowest bits) 0x70 = 112. Highest bit set, so continue. 03 = 0x03 * 128, makes 384. Total 112 + 3 * 128 + 1 = 497

3 byte example:
93 a0 01, means, going from left to right:
	93 => unset highest bit => 0x13 = 19, and continu
	a0 => unset highest bit => 0x20 = 32, so 32 * 128, and continu
	01 => 0x01 = 1, so 1 * 128 * 128, and stop
	Total 19 + 32 * 128 + 1 * 128 * 128 = 20499
'''


# Functions:


def readandremoveNfirstbytes(myba, N):
	res = myba[0:N]
	del myba[0:N]
	return res

def readandremoveVINT(myba):

	# Read and return "vint" from the front of myba (my byte array), and remove the vint from the (global) bytearray

	i = 0 # start at first byte
	result = 0
	weight = 1 # we start at weight 1 for the first 'septet' (7-bit byte), and mutiply with 128 (not 256)

	while True:
		if ba[i]<128:
			# most significant bit NOT set, so last entry
			result += weight * ba[i]
			i += 1
			break	# done
		else:
			# most signifcant bit is set, so we'll have to continu
			result += weight * (ba[i]-128)
			weight *= 128
			i += 1
	del myba[0:i] # remove from start 0, up to i (so: including i-1)
	return result

# MAIN

# Open file passed as argument, and put into a bytearray
fh = open(sys.argv[1],"rb")
ba = bytearray(fh.read())

# Is it a rar?

# Rar4:
# Just for comparison this is RAR 4.x 7 byte length signature: 0x52 0x61 0x72 0x21 0x1A 0x07 0x00.
# https://www.forensicswiki.org/wiki/RAR


# Older rar: 0x 52 45 7E 5E 


rar5sigdefinition = [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x01, 0x00] # RAR 5.0 signature consists of 8 bytes: 0x52 0x61 0x72 0x21 0x1A 0x07 0x01 0x00
# Get first 8 bytes from the bytearray:
rarsignature = readandremoveNfirstbytes(ba,8)
i = 0

# Let's count how many bytes match:
while i < 8:
	if rar5sigdefinition[i] != rarsignature[i]:
		# No match, so ...
		break
	i += 1
print "Matching i", i

# ... which results in:
if i < 3:
	print "Not a rar file at all"
	sys.exit(-1)
elif i == 6:
	print "A rar4 file, not yet supported"
elif i < 8:
	print "A rar file, but not a RAR5 file"
	sys.exit(-1)

	
# Proceeed with the other fields:

crc32 = readandremoveNfirstbytes(ba,4) # 32bits so 4 bytes

headersize = readandremoveVINT(ba)
headertype = readandremoveVINT(ba)
headerflags = readandremoveVINT(ba)
extraareasize= readandremoveVINT(ba)
archiveflags = readandremoveVINT(ba)

if archiveflags & 2 :
	volumenumber = 1 + readandremoveVINT(ba)
else:
	# first volume, aka 1
	volumenumber = 1

print "volumenumber is", volumenumber

#print "... and it's done"




# Old / unused stuff:

def ReadVint(myba, start):

	# Read and return "vint" from myba (my byte array), starting at start. Leave the byte array intact (so: non-destructive reading)

	i = start
	result = 0 # value of vint
	weight = 1 # we start at weight 1 for the first 'septet' (7-bit byte), and mutiply with 128 (not 256) for next septet

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

