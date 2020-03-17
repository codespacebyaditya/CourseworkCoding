#!/usr/bin/env python3

#import the required packages from BioPython
import re
from Bio import SeqIO
#import itertools for taking slices of the list
import itertools

#Store the reads in 2 different objects, namely leftreads and rightreads
leftreads= SeqIO.parse ("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq","fastq")

rightreads=SeqIO.parse ("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq","fastq")

#An empty object is created so that reads from R1 and R2 fastq files can be appended using the append function
seq=[]
#Use zip to iterate the reads parallely from both fastq files

#Since the reads are to be matched and written in a file, create a .fasta file to store the reads. The name of the output FASTA file is specified.
output= open("interleaved.fasta","w")

for l, r in zip(leftreads, rightreads):
    seq.append (l)
    seq.append (r)

#Use Seq InputOutput from Bio to write a FASTA file which includes object seq which holds the left and right reads.
SeqIO.write (seq, output, "fasta")

