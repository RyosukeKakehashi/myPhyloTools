#! /usr/bin/env python

import argparse
import re
import sys

parser = argparse.ArgumentParser(description='This script separates a fasta file according to a partition file. A partition file with RAxML style is acceptable.')
parser.add_argument('input', help='specify a name of fasta file.')
parser.add_argument('-p', '--part', required=True, help='specify a name of a partition file.')
args = parser.parse_args()

with open(args.input, mode='r') as f:
    infile = f.read().strip()
    filemod = re.sub('(>\w+)\n', r'\1@\n', infile)
    filelist = filemod.replace('\n', '').replace('>', '\n>').replace('@', '\n').strip().split('\n')
    seqname = []
    seqs = []
    for l in filelist:
        if l.startswith('>'):
            if re.compile('\W').search(l.lstrip('>')):
                print('Error. Only numbers, alphabets and underscores are acceptable for sequence name!')
                sys.exit()
            seqname.append(l.strip())
        else:
            seqs.append(l.strip())

partnamlst = []
with open(args.part, mode='r') as f:
    part = f.read().strip().split('\n')
    for i, l in enumerate(part):
        tmp = l.split('=')
        partnam = re.sub(r'\w+,', '', tmp[0])
        partnamlst.append(partnam.strip())
        partreg = tmp[1].replace('\\', '%').strip()
        cont1 = re.findall('\d+-\d+%3', partreg)
        del_cont1 = re.sub(r',* *\d+-\d+%3,* *', '', partreg)
        cont2 = re.findall('\d+-\d+', del_cont1)
        del_cont2 = re.sub(r',* *\d+-\d+,* *', '', del_cont1)

        if len(cont1) != 0:
            cont1txt = ''
            for m in cont1:
                rang = m.rstrip('%3').split('-')
                ranglist = list(range(int(rang[0]), int(rang[1]) + 1, 3))
                cont1txt += ',' + ','.join(map(str, ranglist))
            del_cont2 += ',' + cont1txt
        if len(cont2) != 0:
            cont2txt = ''
            for m in cont2:
                rang = m.split('-')
                ranglist = list(range(int(rang[0]), int(rang[1]) + 1))
                cont2txt += ',' + ','.join(map(str, ranglist))
            del_cont2 += ','+ cont2txt

        part[i] = del_cont2


s = ''
for i, l in enumerate(seqs):
    for j, m in enumerate(part):
        s += '%' + partnamlst[j] + seqname[i] + '#'
        for n in m.strip(',').split(','):
            s += l[int(n) - 1]
        s += '\n'

slist = s.split('\n')
for l in partnamlst:
    with open(l + '.fasta', mode='w') as f:
        outlst = list(filter(lambda x: x.startswith('%' + l), slist))
        out = '\n'.join(outlst).replace('%' + l, '').replace('#', '\n')
        f.write(out)
