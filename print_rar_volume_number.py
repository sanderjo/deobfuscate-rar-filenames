#!/usr/bin/env python3

# works for rar5 and rar3/rar4 format


import sys
import os


# Rar4 format: https://www.forensicswiki.org/wiki/RAR
# Rar5 format: https://www.rarlab.com/technote.htm



# Functions:


def readandremoveNfirstbytes(myba, N):
	res = myba[0:N]
	del myba[0:N]
	return res

def readandremoveVINT(myba):

	# Read and return "vint" from the front of myba (my byte array), and remove the vint from the (global) bytearray


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

# Open file passed as argument
fh = open(sys.argv[1],"rb")
# To save memory: we only need the first 250 or so bytes for the rar4/rar5 signature, and rar5 info.
ba = bytearray(fh.read(250))


# Is it a rar?

rar4sigdefinition = [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x00] # RAR 4.x 7 byte length signature: 0x52 0x61 0x72 0x21 0x1A 0x07 0x00.
rar5sigdefinition = [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x01, 0x00] # RAR 5.0 signature consists of 8 bytes: 0x52 0x61 0x72 0x21 0x1A 0x07 0x01 0x00

# Check rar signature at beginning of the rar file:
israr4 = ba[:len(rar4sigdefinition)] == bytearray(rar4sigdefinition)
israr5 = ba[:len(rar5sigdefinition)] == bytearray(rar5sigdefinition)

#print("rar4 and rar5", israr4, israr5)

volumenumber = -1
if israr4:
	print("rar3/rar4")
	# Let's find the numbering scheme
	# ba still contains the first 250 bytes
      
	HEAD_FLAGS_LSB = ba[10]	# LSB = Least Significant Byte
	if HEAD_FLAGS_LSB & 0x10 :
		print("New Numbering Scheme")
	else:
		print("Old Numbering Scheme")



	# It's a rar4, which has the volume number at the end of the rar file 
        # ... warning: hacked together:
	# From the end of the file, we need about 20 bytes
	fh.seek(-20, os.SEEK_END)
	# read into bytearray
	ba = bytearray(fh.read())
	volumenumber = 1 + ba[-9] + 256 * ba[-8] 



elif israr5:
	print("rar5")
	print("New Numbering Scheme")
	# It's a rar5
	# rar5 has the volume number in the beginning of the rar file, after some other (variable length) info:
	# So process them:
	rarsignature = readandremoveNfirstbytes(ba,8)
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

else:
	print("Not a rar file")

print("volumenumber is", volumenumber)
sys.exit(0)


