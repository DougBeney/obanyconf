#!/usr/bin/env python3

import anymarkup
import sys

def file2str(fname):
    with open(fname, 'r') as file:
        data = file.read()
    return data

def saveBytes(bytes, fname):
    with open(fname, 'w') as file:
        file.write(bytes.decode('utf-8'))

if len(sys.argv) < 3:
    print("Gimme more args!")
    print("Correct Usage: obanyconf [input file] [output file]")
    sys.exit()

# File
fname = sys.argv[1]
fstr  = file2str(fname)
fobj  = anymarkup.parse(fstr)

fobj['@xmlns'] = "http://openbox.org/3.4/rc"
fobj['@xmlns:xi'] ="http://www.w3.org/2001/XInclude"

newObj = {}
newObj['openbox_config'] = fobj

out_fname = sys.argv[2]

saveBytes(anymarkup.serialize(newObj, 'xml'), out_fname)
