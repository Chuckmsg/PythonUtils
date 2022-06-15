#!/usr/bin/python
import sys
import os
import random
 
if len(sys.argv) == 3:
    filename = str(sys.argv[1])
    lenstr =sys.argv[2]
    if lenstr[0] == '0' and lenstr[1] == 'x':
        filelen = int(lenstr,16)
    else:
        filelen = int(lenstr)
    with open(filename, 'wb') as f:
        count = 0
        while (count < filelen):
            buf = (random.randint(0,255)).to_bytes(length = 1, byteorder='little', signed=False)
            f.write(buf)
            count = count + 1
    f.close()
else:
    print("fill file:")
    print("python *.py filename filelen")