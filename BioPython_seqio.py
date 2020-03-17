#!/usr/bin/env python3
#BioPython_seqio.py

from Bio.Seq import Seq
from Bio import SeqIO
import sys

def Seqio (fasta_file):
    '''Seqio takes in fasta file and generates its reverse complement which is stored as a new record
    '''
    inputf= SeqIO.parse (fasta_file, 'fasta')
    outf= []
    for i in inputf:
        new_rec= i.seq
        new_rec= new_rec.reverse_complement()
        i.seq= new_rec
        outf.append(i)
    return (outf)

if __name__=='__main__':
    if len (sys.argv) -1 <2:
        raise Exception ("At least 2 arguments needed")
    output= Seqio (sys.argv[1])
    '''SeqIO.write is used to write the file in the desired format
    '''
    SeqIO.write (output, sys.argv[2], "fasta")
