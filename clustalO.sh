#!/usr/bin/env bash
# clustalO.sh

# clutsal command
clustalo -i "apoe_aa.fasta" -o "MSAlignmentResults" -v 
1>alignment.log 2>alignment.err
