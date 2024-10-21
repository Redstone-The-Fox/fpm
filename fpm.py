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
args = parser.parse_args()
if str(args.install) in repo:
    os.system(f'git clone {repo[args.install]}')
else:
    print(f'package not found: {args.install}')