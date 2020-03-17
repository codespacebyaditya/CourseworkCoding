#!/usr/bin/env python3
#Biopython_genbnk.py

from Bio import Entrez 
from Bio import SeqIO
'''Enter email to fetch Entrez results
'''
Entrez.email = "singh.adityas@northeastern.edu"

seq = []
'''Seq initialised to store the sequence and operations to be performed
'''
with Entrez.efetch (db="nucleotide", rettype="gb", retmode="text", id="515056") as handle:
    seqRecord= SeqIO.read (handle, "gb")
    seq.append(seqRecord)

with Entrez.efetch (db="nucleotide", rettype="gb", retmode="text", id="J01673.1") as handle:
    seqRecord= SeqIO.read (handle, "gb")
    seq.append(seqRecord)

for entry in seq:
    print ("Sequence Name: {}".format(entry.name))
    print ("entry.seq")
    ''' The entries fetched will display type, location and strand information
    '''
    for i in entry.features:
        print ("{}\t{}\t{}\t".format(i.type, i.location, i.strand))
