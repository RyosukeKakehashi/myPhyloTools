#! /usr/bin/env python

from scipy.stats import chi2
import argparse
import re
import sys

parser = argparse.ArgumentParser(description='This script performs chi-square test for compositional homogeneity of characters.')
parser.add_argument('input', help='specify a file name.')
parser.add_argument('-t', '--type', default='d', required=True, help='select a character type, dna (d) or amino acid (a). Default is "-t d"')
parser.add_argument('-m', '--mode', default='w', required=True, help='select a test mode, whole (w) or partial (p). Default is "-m w"')
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
            seqs.append(l.lower().strip().replace('-', ''))

print('Test method is chi-squared.')

if args.type == 'n':
    numA = 0
    numT = 0
    numG = 0
    numC = 0
    
    numseqs = len(seqs)
    df = (numseqs - 1) * 3
    
    arr = []
    for l in seqs:
        tmp = []
        tmpA = l.count('a')
        tmpT = l.count('t')
        tmpG = l.count('g')
        tmpC = l.count('c')
        tmp.append(tmpA)
        tmp.append(tmpT)
        tmp.append(tmpG)
        tmp.append(tmpC)
        arr.append(tmp)
        numA += tmpA
        numT += tmpT
        numG += tmpG
        numC += tmpC
    
    exA = numA / numseqs
    exT = numT / numseqs
    exG = numG / numseqs
    exC = numC / numseqs
    
    if args.mode == 'w':
        chi = 0
        for l in arr:
            chi += ((l[0] - exA) ** 2) / exA + ((l[1] - exT) ** 2) / exT + ((l[2] - exG) ** 2 ) / exG + ((l[3] - exC) ** 2 ) / exC
    
        print('Number of sequences: ' + str(numseqs))
        print('Degree of freedom: ' + str(df))
        print('Chi-square statistic: ' + str(chi))
        print('p-value: ' + str(chi2.sf(x = chi, df = df)))
        print('Expected content (A, T, G, C): ' + str(exA) + ', ' + str(exT) + ', ' + str(exG) + ', ' + str(exC))
    elif args.mode == 'p':
        count = 0
        failseq = []
        for i, l in enumerate(arr):
            chi = ((l[0] - exA) ** 2) / exA + ((l[1] - exT) ** 2) / exT + ((l[2] - exG) ** 2 ) / exG + ((l[3] - exC) ** 2 ) / exC
            pvalue = chi2.sf(x=chi, df=3)
            if pvalue < 0.05:
                count += 1
                failseq.append(seqname[i].lstrip('>'))
            print(seqname[i] + ': p-value = ' + str(pvalue))
        print('-' * 100)
        print('Number of sequences: ' + str(numseqs))
        print('Expected content (A, T, G, C): ' + str(exA) + ', ' + str(exT) + ', ' + str(exG) + ', ' + str(exC))
        print('The following ' + str(count) + ' sequences failed to pass the test (p < 0.05).')
        print(', '.join(failseq))


elif args.type == 'a':
    numA = 0
    numR = 0
    numN = 0
    numD = 0
    numC = 0
    numQ = 0
    numE = 0
    numG = 0
    numH = 0
    numI = 0
    numL = 0
    numK = 0
    numM = 0
    numF = 0
    numP = 0
    numS = 0
    numT = 0
    numW = 0
    numY = 0
    numV = 0
    
    numseqs = len(seqs)
    df = (numseqs - 1) * 19
    
    arr = []
    for l in seqs:
        tmp = []
        tmpA = l.count('a')
        tmpR = l.count('r')
        tmpN = l.count('n')
        tmpD = l.count('d')
        tmpC = l.count('c')
        tmpQ = l.count('q')
        tmpE = l.count('e')
        tmpG = l.count('g')
        tmpH = l.count('h')
        tmpI = l.count('i')
        tmpL = l.count('l')
        tmpK = l.count('k')
        tmpM = l.count('m')
        tmpF = l.count('f')
        tmpP = l.count('p')
        tmpS = l.count('s')
        tmpT = l.count('t')
        tmpW = l.count('w')
        tmpY = l.count('y')
        tmpV = l.count('v')
        tmp.append(tmpA)
        tmp.append(tmpR)
        tmp.append(tmpN)
        tmp.append(tmpD)
        tmp.append(tmpC)
        tmp.append(tmpQ)
        tmp.append(tmpE)
        tmp.append(tmpG)
        tmp.append(tmpH)
        tmp.append(tmpI)
        tmp.append(tmpL)
        tmp.append(tmpK)
        tmp.append(tmpM)
        tmp.append(tmpF)
        tmp.append(tmpP)
        tmp.append(tmpS)
        tmp.append(tmpT)
        tmp.append(tmpW)
        tmp.append(tmpY)
        tmp.append(tmpV)
        arr.append(tmp)
        numA += tmpA
        numR += tmpR
        numN += tmpN
        numD += tmpD
        numC += tmpC
        numQ += tmpQ
        numE += tmpE
        numG += tmpG
        numH += tmpH
        numI += tmpI
        numL += tmpL
        numK += tmpK
        numM += tmpM
        numF += tmpF
        numP += tmpP
        numS += tmpS
        numT += tmpT
        numW += tmpW
        numY += tmpY
        numV += tmpV
    
    exA = numA / numseqs
    exR = numR / numseqs
    exN = numN / numseqs
    exD = numD / numseqs
    exC = numC / numseqs
    exQ = numQ / numseqs
    exE = numE / numseqs
    exG = numG / numseqs
    exH = numH / numseqs
    exI = numI / numseqs
    exL = numL / numseqs
    exK = numK / numseqs
    exM = numM / numseqs
    exF = numF / numseqs
    exP = numP / numseqs
    exS = numS / numseqs
    exT = numT / numseqs
    exW = numW / numseqs
    exY = numY / numseqs
    exV = numV / numseqs
    

    if args.mode == 'w':
        chi = 0
        for l in arr:
            chi += ((l[0] - exA) ** 2) / exA + ((l[1] - exR) ** 2) / exR + ((l[2] - exN) ** 2 ) / exN + ((l[3] - exD) ** 2 ) / exD + ((l[4] - exC) ** 2) / exC + ((l[5] - exQ) ** 2) / exQ + ((l[6] - exE) ** 2 )/ exE + ((l[7] - exG) ** 2 ) / exG + ((l[8] - exH) ** 2) / exH + ((l[9] - exI) ** 2) / exI + ((l[10] - exL) ** 2 ) / exL + ((l[11] - exK) ** 2 )/ exK + ((l[12] - exM) ** 2) / exM + ((l[13] - exF) ** 2) / exF + ((l[14] - exP) ** 2 ) / exP + ((l[15] - exS) ** 2 ) / exS + ((l[16] - exT) ** 2) / exT + ((l[17] - exW) ** 2) / exW + ((l[18] - exY) ** 2 ) / exY + ((l[19] - exV) ** 2 ) / exV
    
        print('Number of sequences: ' + str(numseqs))
        print('Degree of freedom: ' + str(df))
        print('Chi-square statistic: ' + str(chi))
        print('p-value: ' + str(chi2.sf(x = chi, df = df)))
        print('Expected content (A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V): ' + str(exA) + ', ' + str(exR) + ', ' + str(exN) + ', ' + str(exD)+ ', ' + str(exC) + ', ' + str(exQ) + ', ' + str(exE) + ', ' + str(exG) + ', ' + str(exH) + ', ' + str(exI) + ', ' + str(exL) + ', ' + str(exK) + ', ' + str(exM) + ', ' + str(exF) + ', ' + str(exP) + ', ' + str(exS) + ', ' + str(exT) + ', ' + str(exW) + ', ' + str(exY) + ', ' + str(exV))
    elif args.mode == 'p':
        count = 0
        failseq = []
        for i, l in enumerate(arr):
            chi = ((l[0] - exA) ** 2) / exA + ((l[1] - exR) ** 2) / exR + ((l[2] - exN) ** 2 ) / exN + ((l[3] - exD) ** 2 ) / exD + ((l[4] - exC) ** 2) / exC + ((l[5] - exQ) ** 2) / exQ + ((l[6] - exE) ** 2 )/ exE + ((l[7] - exG) ** 2 ) / exG + ((l[8] - exH) ** 2) / exH + ((l[9] - exI) ** 2) / exI + ((l[10] - exL) ** 2 ) / exL + ((l[11] - exK) ** 2 )/ exK + ((l[12] - exM) ** 2) / exM + ((l[13] - exF) ** 2) / exF + ((l[14] - exP) ** 2 ) / exP + ((l[15] - exS) ** 2 ) / exS + ((l[16] - exT) ** 2) / exT + ((l[17] - exW) ** 2) / exW + ((l[18] - exY) ** 2 ) / exY + ((l[19] - exV) ** 2 ) / exV
            pvalue = chi2.sf(x=chi, df=19)
            if pvalue < 0.05:
                count += 1
                failseq.append(seqname[i].lstrip('>'))
            print(seqname[i] + ': p-value = ' + str(pvalue))
        print('-' * 100)
        print('Number of sequences: ' + str(numseqs))
        print('Expected content (A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V): ' + str(exA) + ', ' + str(exR) + ', ' + str(exN) + ', ' + str(exD)+ ', ' + str(exC) + ', ' + str(exQ) + ', ' + str(exE) + ', ' + str(exG) + ', ' + str(exH) + ', ' + str(exI) + ', ' + str(exL) + ', ' + str(exK) + ', ' + str(exM) + ', ' + str(exF) + ', ' + str(exP) + ', ' + str(exS) + ', ' + str(exT) + ', ' + str(exW) + ', ' + str(exY) + ', ' + str(exV))
        print('The following ' + str(count) + ' sequences failed to pass the test (p < 0.05).')
        print(', '.join(failseq))

