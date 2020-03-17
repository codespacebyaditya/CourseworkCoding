#!/usr/bin/env python3
#BioPython_seq.py
#Import Seq, SeqRecord and SeqIO. These are instantiated, they're BioPython classes
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Alphabet import generic_dna
#Initialize an empty array (a list)
sequences= list()
my_seq1= SeqRecord(Seq("aaaatgggggggggggccccgtt", generic_dna), id="12345", description="example1")
#Add the sequences to the array
sequences.append(my_seq1)
#Write the SeqRecords within the list sequences as a genbank file with .gb extension file
SeqIO.write (sequences, "biopython_seq.gb", "gb")
