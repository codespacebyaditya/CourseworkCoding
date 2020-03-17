#!/usr/bin/env bash
#alignPredicted.sh

#blastp is used with pep file which contains the peptides as input and parameters are set as instructed.

blastp -query ./Trinity.fasta.transdecoder.pep -db swissprot -evalue 1e-10 -num_threads 4 -outfmt "6 qseqid sacc qlen slent length nident pident evalue stitle" 1>alignPredicted.txt 2>alignPredicted.err
