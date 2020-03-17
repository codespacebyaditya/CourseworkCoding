#!/usr/bin/env python3
#find_dmel_orf.py
#Import the needed packages from Biopython
from Bio import SeqIO

#import re i.e regular expressions for searching the FASTA file
import re
from Bio.Seq import Seq

for record in SeqIO.parse ("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
    if re.match ("^\d{1}\D*$", record.id):
        dna=record.seq
        rna=dna.transcribe()

        #Process of transcription
        orf= re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str (rna)).group()

        #Search the ORF for start and stop codon
        protein=Seq(orf)
        protein=protein.translate()

        #translation of RNA to protein
        print (protein)

