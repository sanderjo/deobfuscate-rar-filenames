#!/usr/bin/env python3
# but works with python 2.7 too

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

import math


x=40500
print("x is",x)

numberofseptets = math.ceil(math.log(x,128))
print("numberofseptets", numberofseptets)
power = numberofseptets -1

print("Go:")

while power >= 0:

	print("Remaining x is", x)
	newbase = int(math.pow(128, power))
	print("newbase", newbase)
	septetvalue = int(x/newbase)
	print("septetvalue", septetvalue)
	x = x - septetvalue*newbase # the remainder
	power = power-1

print("KLAAR")





