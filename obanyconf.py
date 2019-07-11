#!/usr/bin/env python3

import sys
import argparse
import anymarkup

XMLNS_DEFAULT = 'http://openbox.org/3.4/rc'
XMLNSXI_DEFAULT = 'http://www.w3.org/2001/XInclude'


def file_2_str(fname):
    """Reads a file and returns it as a string"""
    with open(fname, 'r') as file:
        data = file.read()
    return data


def save_bytes(bytes_str, fname):
    """Takes bytes and saves them to a file"""
    with open(fname, 'w') as file:
        file.write(bytes_str.decode('utf-8'))

parser = argparse.ArgumentParser(description='Use any configuration type with OpenBox')
parser.add_argument('input', type=str,
                    help='Input file')
parser.add_argument('output', type=str, nargs='?',
                    help='Output file')
parser.add_argument('--ext', '-e', default="xml",
                    help='Output file type (Default = \'xml\')')
parser.add_argument('--stdout', action='store_true',
                    help='Print to stdout instead of saving to a file')
parser.add_argument('--skip-check', '-s', action='store_true',
                    help='Don\'t run standard configuration/XML checks')
parser.add_argument('--verbose', '-v', action='store_true',
                    help='Show more information')

args = parser.parse_args()

INPUT_CONFIG = args.input
OUTPUT_CONFIG = args.output

try:
    INPUT_CONFIG_STR = file_2_str(INPUT_CONFIG)
except Exception as e:
    print("Failed to read", INPUT_CONFIG)
    if args.verbose:
        print(e.get('message', e))
    else:
        print("Use the --verbose flag to get more information")
    exit(1)

try:
    INPUT_CONFIG_OBJ = anymarkup.parse(INPUT_CONFIG_STR)
except Exception as e:
    print("Failed to parse", INPUT_CONFIG)
    if args.verbose:
        print(e.get('message', e))
    else:
        print("Use the --verbose flag to get more information")
    exit(1)

NEW_OBJ = {}

# Handy check that will ensure xmlns and xmlns:xi is set.
# If it is not set, it will automatically be set to a sane value.
# This also removes the need for the user to include openbox_config as
# a top-level.
if not args.skip_check:
    if INPUT_CONFIG_OBJ.get('openbox_config', False):
        INPUT_CONFIG_OBJ['openbox_config']['@xmlns'] = \
            INPUT_CONFIG_OBJ['openbox_config'].get('@xmlns', XMLNS_DEFAULT)
        INPUT_CONFIG_OBJ['openbox_config']['@xmlns:xi'] = \
            INPUT_CONFIG_OBJ['openbox_config'].get('@xmlns:xi', XMLNSXI_DEFAULT)

        NEW_OBJ = INPUT_CONFIG_OBJ
    else:
        INPUT_CONFIG_OBJ['@xmlns'] = \
            INPUT_CONFIG_OBJ.get('@xmlns', XMLNS_DEFAULT)
        INPUT_CONFIG_OBJ['@xmlns:xi'] = \
            INPUT_CONFIG_OBJ.get('@xmlns:xi', XMLNSXI_DEFAULT)

        NEW_OBJ['openbox_config'] = INPUT_CONFIG_OBJ

try:
    DATA = anymarkup.serialize(NEW_OBJ, args.ext)
except Exception as e:
    print(e)
    exit(1)

if args.stdout:
    print(DATA.decode('utf-8'))
else:
    save_bytes(DATA, OUTPUT_CONFIG)
