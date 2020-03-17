#!/usr/bin/env bash
#Quast.sh



DIRECTORY="Quast/"
#An output directory called quast is created
mkdir -p $DIRECTORY

function run_quast {
/usr/bin/quast.py \
    -o $DIRECTORY \
    --threads 6 \
    -s \
    Rhodobacter/scaffolds.fasta

}
run_quast

#run_quast 1>quast.log 2>quast.err
