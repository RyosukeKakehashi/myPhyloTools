#! /usr/bin/env python

import argparse
import re

parser = argparse.ArgumentParser(description='This script converts format of partition file between raxml and nexus.')
parser.add_argument('input', help='specify a input file name.')
parser.add_argument('-t', '--type', default='DNA', help='Specify the data type. This option is used for raxml output.')
args = parser.parse_args()

with open(args.input, mode='r') as f:
    infile = f.read()

infileclean = infile.strip()
infilelist = infileclean.split('\n')

outlist = []
if infileclean.startswith('#') or infileclean.lower().startswith('begin'):
    flg = 0
    print('Input file is recognised as NEXUS style.')
    for line in infilelist:
        tmp = line.strip()
        if tmp.lower().startswith('charset'):
            tmp_mod = tmp.replace('charset','').replace(';','').strip()
            tmp = re.sub('(\d) (\d)', r'\1,\2',tmp_mod)
            outlist.append(args.type + ', ' + tmp)
else:
    flg = 1
    print('Input file is recognised as RAxML style.')
    outlist.append('#nexus\nbegin sets;')
    for line in infilelist:
        tmp = line.strip() + ';'
        tmp_mod = re.sub('^\w+, *', r'', tmp)
        tmp = re.sub(', *', r' ', tmp_mod)
        outlist.append('    charset ' + tmp)

    outlist.append('    charpartition mine = \nend;')

outtext = "\n".join(outlist)

if flg == 0:
    with open('raxml.partition', mode='w') as f:
        f.write(outtext)

elif flg == 1:
    with open('nexus.partition', mode='w') as f:
        f.write(outtext)
