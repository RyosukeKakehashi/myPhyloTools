#! /usr/bin/env python

import argparse
import re
import sys

parser = argparse.ArgumentParser(description='This script concatenates multiple fasta files.')
parser.add_argument('input', help='specify a file name containing input fasta files.')
parser.add_argument('-o', '--output', default='concatenate.fasta', help='specify output file name. Default = concatenate.fasta')
parser.add_argument('-p', '--part', action='store_true', help='optional. This option constructs a partition file.')
args = parser.parse_args()

# Import fasta file list
filelist = []
with open(args.input, mode='r') as f:
	for line in f.readlines():
		if line.strip() != "":
			filelist.append(line.strip())

# Read files
fileslist = []
for l in filelist:
	with open(l, mode='r') as f:
		fileslist.append(f.read())

for i, l in enumerate(fileslist):
	tmp = re.sub('(>\w+)\n', r'\1@', l)
	fileslist[i] = tmp.replace(' ', '').replace('\n', '').replace('>', '\n>').strip().replace('@', '\n').split('\n')

# Check the number of taxa.
taxnum = len(fileslist[0])
#print("%d taxa are included."%(taxnum / 2) )
for l in fileslist[1:]:
	if taxnum != len(l):
		print("Number of taxa is different!!")
		sys.exit()

# Check the taxon set.
taxnam = ""
for i in fileslist[0]:
	if i.startswith(">"):
		taxnam += i

for i in fileslist[1:]:
	tax = ""
	for j in i:
		if j.startswith(">"):
			tax += j
	if taxnam != tax:
		print("Taxon name is different!!")
		sys.exit()

# Concatenate sequences
conseqlist = list(zip(*fileslist))
for i, l in enumerate(conseqlist):
	if l[0].startswith(">"):
		conseqlist[i] = l[0] + "\n"
	else:
		conseqlist[i] = "".join(l) + "\n"

# Check sequence length.
seqlen = len(conseqlist[1])
for l in conseqlist:
	if l.startswith(">"):
		continue
	else:
		if seqlen != len(l):
			print("Sequence length is different!!")
			sys.exit()

# Write sequences to file.
with open(args.output, mode='w') as f:
	f.write("".join(conseqlist))

# Construct partition file.
if args.part:
	tlen = 0
	part = ""
	for fi, length in zip(filelist, fileslist):
		seqlength = len(length[1])
		part += "DNA, " + fi + " = " + str(tlen + 1) + "-" + str(tlen + seqlength) + "\n"
		tlen += seqlength

	outpart = args.output + ".partition"
	with open(outpart, mode='w') as f:
		f.write(part)
