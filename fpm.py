#!/usr/bin/env python
try:
    from repo import repo
    import requests
    import argparse
    import os
except ModuleNotFoundError:
    exit('one or more modules were not found')

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--install', help='installs a package')
parser.add_argument('-v','--version', help='outputs version', action='store_true')
args = parser.parse_args()
if args.version:
    exit('FPM Version 0.1')
if str(args.install) in repo:
    os.system(f'{repo[args.install]}')
else:
    print(f'package not found: {args.install}')