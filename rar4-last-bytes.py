import sys
import os

file = sys.argv[1]

print("tool for rar4-only!")

with open(file, 'rb') as fh:
    # From the end of the file, we need about 20 bytes
    fh.seek(-20, os.SEEK_END)
    # read into bytearray
    ba = bytearray(fh.read())
    print("len ba is", len(ba))
    pos = len(ba)
    volumenumber = 1 + ba[pos-9] + 256 * ba[pos-8]
    print("volume number is", volumenumber)
