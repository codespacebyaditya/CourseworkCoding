#!/usr/bin/env python
#headers_to_file.py

import re

dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'

line_count=0
seq= ''

with open (dmel_genome_path) as dmel_genome:
    for line in dmel_genome:
        if line_count<50:
            #Scan the FASTA line and look for >
            if re.match ('>', line):
                #Sequence gets the header file
                seq+= line
                line_count+=1

with open ("dmel_headers.txt", 'w')as out:

    out.write (seq)

