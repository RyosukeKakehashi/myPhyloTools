# List of tools for phylogenetic analysis

The following scripts were developed by Python 3.8.

### ConcatFas.py

A script to concatenate multiple fasta files.

Usage: python ConcatFas.py *input_file*

Input file is a list of fasta files. Please specify path to the files, if files are not in the current directory. Each file should be described in one line. Default output file name is *concatenate.fasta*. You can change the output file name by '-o' option. This script can also construct a partition file with '-p' option.

Note that fasta files with CR+LF newline characters may cause problems.

### ConvPart.py
A script to convert a partition file between raxml and nexus style. This script automatically recognises input file style, and converts to another style. 

Usage: python ConvPart.py *input_file*

Note that some information (e.g., substitution model) are ignored, when converting from nexus to raxml style. 

### GBstrip.py
A script to extract each gene (strictly, cds, ribosomal RNA, and transfer RNA) sequence from a GenBank file. This script can treat a GenBank file containing multiple accessions, and separate into output files by each accession.

Usage: python GBstrip.py *input_file*

### SeqSplitter.py
A script to divide a fasta file into separate partition files according to the partition file. The partition file with RAxML style is acceptable.

Usage: python SeqSplitter.py *input_fasta_file* -p *input_partition_file*

### HomogeneityTest.py
A script to test for compositional homogeneity of characters using chi-square test.

Usage: python HomogeneityTest.py *input_fasta_file*

This script implements two modes of chi-square test: 1) comparing all sequences at once (default mode), and 2) comparing each sequence with the overall composition (by adding an option "-m p"). In default, this script treat sequence characters as nucleotides. When testing amino acid sequences, users need to add a option "-t a". Note that ambiguous characters (e.g., N, R, Y etc. in nucleotides) are ignored in this test.

This script requires the following package:

- scipy

## Contributor
### Ryosuke Kakehashi
