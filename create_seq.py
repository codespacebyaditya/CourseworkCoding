#!/usr/bin/env python3
#create_seq.py
#Import Seq, SeqRecord and SeqIO. These are instantiated, they'r eBioPython classes
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
#Initialize an empty array (a list)
sequences= list()
#Use (intantiate) SeqRecord as my_seq1 and 2. Notice SeqRecord requires a Seq, so we just instantiate the Seq within the constructor for SeqRecord.
my_seq1= SeqRecord(Seq("ATGACACTGGT"), id="seq1", description="kmer1")
my_seq2= SeqRecord(Seq("AGTACATGGC"), id="seq2", description="kmer2")
#Add the sequences to the array
sequences.append(my_seq1)
sequences.append(my_seq2)
#Write the SeqRecords within the list sequences as a fasta file
SeqIO.write (sequences, "kmers.fasta", "fasta")

