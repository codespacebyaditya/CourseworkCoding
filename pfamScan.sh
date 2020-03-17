#!/usr/bin/env bash
#pfamScan.sh
hmmscan --cpu 4 --domtblout pfam.domtblout /scratch/SampleDataFiles/Pfam-A.hmm Trinity.fasta.transdecoder_dir/longest_orfs.pep 1>pmanScan.log 2>pfamScan.err &
