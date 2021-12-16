#! /usr/bin/env python

import argparse
import re
import sys

parser = argparse.ArgumentParser(description='This script extracts genes from GenBank files.')
parser.add_argument('input', help='specify a file name.')
parser.add_argument('-o', '--output', default='gbs_', help='specify prefix of output file name. Default is "-o gbs_"')
args = parser.parse_args()

with open(args.input, encoding='utf-8') as f:
	infile = f.read()
	infilelst = infile.replace('/product', '/gene').split('\n')
	cds = 0
	rrn = 0
	trn = 0
	ori = 0
	gene = []
	regst = []
	regen = []
	seq = ""
	out = []
	lst = []
	for line in infilelst:
		if line.strip().startswith("ACCESSION"):
			accs = line.strip().lstrip("ACCESSION").strip()
		elif line.strip().startswith("ORGANISM"):
			org = line.strip().lstrip("ORGANISM").strip().replace(' ', '_')
		elif line.strip().startswith("CDS"):
			reg = line.strip().lstrip("CDS").strip().lstrip("complement(").rstrip(")").split("..")
			reg0 = re.sub(r'\D', '', reg[0])
			reg1 = re.sub(r'\D', '', reg[1])
			regst.append(reg0)
			regen.append(reg1)
			cds = 1
		elif line.strip().startswith("rRNA"):
			reg = line.strip().lstrip("rRNA").strip().lstrip("complement(").rstrip(")").split("..")
			reg0 = re.sub(r'\D', '', reg[0])
			reg1 = re.sub(r'\D', '', reg[1])
			regst.append(reg0)
			regen.append(reg1)
			rrn = 1
		elif line.strip().startswith("tRNA"):
			reg = line.strip().lstrip("tRNA").strip().lstrip("complement(").rstrip(")").split("..")
			reg0 = re.sub(r'\D', '', reg[0])
			reg1 = re.sub(r'\D', '', reg[1])
			regst.append(reg0)
			regen.append(reg1)
			trn = 1
		elif line.strip().startswith("/gene"):
			if cds == 1:
				gene.append(line.strip().lstrip("/gene=").strip('"').replace(' ', '_'))
				cds = 0
			elif rrn == 1:
				gene.append(line.strip().lstrip("/gene=").strip('"').replace(' ', '_'))
				rrn = 0
			elif trn == 1:
				gene.append(line.strip().lstrip("/gene=").strip('"').replace(' ', '_'))
				trn = 0
		elif 'ORIGIN' in line:
			ori = 1
		elif '//' not in line and ori == 1:
			seq += line.strip()
			line = f.readline()
		elif '//' in line:
			seqs = re.sub('[0-9]', '', seq.replace(' ', ''))
			for i in range(len(gene)):
				st = int(regst[i]) - 1
				en = int(regen[i])
				name = ">" + accs + "_" + org + "_" + gene[i]
				out.append(name + "#" + seqs[st:en])
			out.sort()
			outtxt = '\n'.join(out)
			with open(args.output + accs + '.fasta', mode='w') as g:
				g.write(outtxt.replace('#', '\n'))
			cds = 0
			ori = 0
			gene = []
			regst = []
			regen = []
			seq = ""
			out = []
			lst.append(accs)
		else:
			continue
