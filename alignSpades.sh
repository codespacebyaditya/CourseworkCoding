#!/usr/bin/env bash
#alignSpades.sh


#filepath="./Paired/"

directory="Rhodobacter/"
#An output directory called Rhodobacter is created

mkdir -p $directory


function align_spades {
nice -n19 python3.4 /usr/local/programs/SPAdes-3.10.0-Linux/bin/spades.py \
    -o $directory \
    -1 Paired/SRR522244_1.paired.fastq \
    -2 Paired/SRR522244_2.paired.fastq \
    --threads 4
}








align_spades 1>spades.log 2>spades.err &
