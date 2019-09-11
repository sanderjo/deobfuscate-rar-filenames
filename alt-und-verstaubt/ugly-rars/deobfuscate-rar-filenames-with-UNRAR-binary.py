#!/usr/bin/env python3
# ... but works with python2.7 too

"""
This program will rename obfuscated rar files to the correct blablabla.partN.rar filenames
Needed if you have no par2 files
"""

import subprocess
import os
import re
import logging
import shlex

logging.basicConfig(level=logging.DEBUG)
logging.debug("Log level is DEBUG")


def rarordernumber(filename):
    """
	returns rar order number if it's a rar file
	and returns None if it's not a rar file
	Line to find, then last parameter: "Details: RAR 5, volume 3"
	"""
    rarcommand = "rar"
    logging.debug("XXX filename 1 is %s", filename)
    filename = filename.replace("'","\'").replace("'","\'")
    logging.debug("XXX filename 2 is %s", filename)

    #command = (rarcommand + " l " + filename).split()
    #command = shlex.split('rar l "{}"'.format(filename))
    '''
    command = '{} l "{}"'.format(rarcommand,filename)
    '''
    print(filename.find('"'))
    if filename.find('"')>=0:
	# there is a " in the filename ... so put ' around the filename
        logging.debug("there is a double-quote in the filename")
        command = "{} l '{}'".format(rarcommand,filename)

    elif filename.find("'")>=0:
        # there is a ' in the filename
        logging.debug("there is a single-quote in the filename")
        command = '{} l "{}"'.format(rarcommand,filename)
    else:
        logging.debug("Nothing special")
        command = '{} l "{}"'.format(rarcommand,filename)


    
    #print("command 1", command)
    
    print("command is ... ",command)
    logging.debug("command is %s", command)
    # p = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    output = os.popen(command).readlines()
    #print(output)
    #output = p.stdout.read()
    ordernumber = None
    for line in output:
        if line.find("Details")>=0:
            ordernumber = line.split()[-1]
        '''
        details = re.findall("Details.*", line)
        if details:
            print("GEVONDEN", details[0].split()[-1])
            # ordernumber = re.findall("Details.*", line.decode("utf-8"))[0].split()[-1]
            print(ordernumber)
        '''
        print("Ordernumber:",ordernumber)
    return ordernumber


# Main

path = "."
for file in os.listdir(path):
    # current_file = os.path.join(path, file)
    # print current_file
    logging.debug("Handling %s", file)
    ordernumber = rarordernumber(file)
    if ordernumber:
        # Yes, a rar file, so rename (put in some padding 0's)
        newname = "blablabla.part" + ('00000'+ordernumber)[-5:] + ".rar"
        logging.debug("Renaming %s to %s", file, newname)
        os.rename(file, newname)
    else:
        logging.debug("Skipping (as not a rar file): %s", file)

