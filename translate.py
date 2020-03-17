#!/usr/bin/env python3
#translate.py
#import Seq
from Bio.Seq import Seq
dna =Seq ("AGTACATTATGACCTACT")
rna= dna.transcribe()
protein=rna.translate()
print (protein)
