# List of tools for phylogenetic analysis

### ConcatFas.py
A script to concatenate multiple fasta files.

Usage: python ConcatFas.py *input_file*

Input file is a list of fasta files. Please specify path to the files, if files are not in the current directory. Each file should be described in one line. Default output file name is *concatenate.fasta*. You can change the output file name by '-o' option. This script can also construct a partition file with '-p' option.

Note that fasta files with CR+LF newline characters may cause problems.

### ConvPart.py
A script to convert a partition file between raxml and nexus style. This script automatically recognises input file style, and converts to another style. 

Usage: python ConvPart.py *input_file*

Note that some information (e.g., substitution model) are ignored, when converting from nexus to raxml style. 


## Contributor(s)
### Ryosuke Kakehashi
