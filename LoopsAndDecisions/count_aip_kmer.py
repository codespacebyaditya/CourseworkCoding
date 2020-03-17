#!/usr/bin/env python3 


#Import the package for regular expressions available for python since we have to match the nucleotides in the fastq file
import re


#Locate the fastq file on Defiance and the sequence is assigned to a variable
sequence= open ('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq','r')


#Line is initialised in order to match ATG or C and then assigned to the kmer dictionary 
line= ' '

#Specify the length of kmers
kmer_length= 6


kmer_dictionary= {}


while line:
#sequence.readline will scan the nucleotide sequences in the fastq files (basically read, as the name suggests)
    line= sequence.readline()
    #Regular expressions used for matching and then for soring it in the kmer dictionary 
    if re.match('^[ATGCN]+$', line): 
        for start in range(0, len(line) - kmer_length):
            kmer= line[start:start +kmer_length]
            kmer_dictionary[kmer]=kmer_dictionary.get (kmer, 0) +1
#Since a text file has to be generated, counted_kmer is used
counted_kmer= ''

for kmer, count in kmer_dictionary.items():
    counted_kmer=("{0}\t{1}\n".format(kmer, count))+ counted_kmer

#counted_kmer is written to a text file with tab spaces and newline characters so that all kmers and teir counts align with each other
with open ("aip_kmers.txt",'w') as out:
     out.write (counted_kmer)
                    
