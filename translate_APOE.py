#!/usr/bin/env python3
# translate_APOE.py

from Bio import SeqIO
from Bio.Seq import Seq

#An empty list is created to store the translated sequence at the end
transcript= []

#Using for and SeqIO to transcribe and then translate the sequence
for record in SeqIO.parse("APOE_refseq_transcript.fasta", "fasta"):
      #A new record is created
        new = record.seq
        #transcription of the DNA sequence
        new = new.transcribe()
        #translation of mRNA to amino acid sequence
        new = new.translate()

        #Restoring in the variable created previously
        record.seq = new
        #For adding the lines, append function is used
        transcript.append(record)

        #SeqIo.write is used to write a new FASTA file 
        SeqIO.write(transcript, "apoe_aa.fasta", "fasta")
