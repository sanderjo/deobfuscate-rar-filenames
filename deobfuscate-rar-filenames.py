#!/usr/bin/env python3
# ... but works with python2.7 too

'''
This program will rename obfuscated rar files to the correct blablabla.partN.rar filenames
Needed if you have no par2 files
'''

import subprocess
import os
import re

debug = True

def rarordernumber(filename):
	'''
	returns rar order number if it's a rar file
	and returns None if it's not a rar file
	Line to find, then last parameter: Details: RAR 5, volume 3
	'''
	rarcommand = 'rar'
	command =(rarcommand + ' l ' + filename).split()
	p = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = p.stdout.read()
	ordernumber = None
	try:
		ordernumber = re.findall("Details.*", output.decode('utf-8'))[0].split()[-1]
	except:
		pass
	return ordernumber

# Main

path = '.'
for file in os.listdir(path):
	#current_file = os.path.join(path, file)
	#print current_file
	print(file)
	ordernumber = rarordernumber(file)
	if ordernumber:
		# Yes, a rar file, so rename
		newname = 'blablabla.part' + ordernumber + '.rar'
		if debug:
			print("Renaming", file, "to", newname)
		os.rename(file, newname)
	else:
		if debug:
			print("Skipping (as not a rar file):", file)




