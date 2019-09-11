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


filename = 'ikke met spaties'




if True:
    rarcommand = "rar"
    #command = (rarcommand + " l " + filename).split()
    command = shlex.split('{} l "{}"'.format(rarcommand,filename))
    print("command is", command)
    p = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.read()
    try:
        ordernumber = re.findall("Details.*", output.decode("utf-8"))[0].split()[-1]
    except:
        pass
    print(ordernumber)


