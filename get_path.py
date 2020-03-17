#!/usr/bin/env python3

# get_path.py

import subprocess
kegg = open('ko.txt')
kegg_ids = {}
out = open('path.txt','w')
err = open('path.err', 'w')
for kegg_line in kegg:
    #Removing line terminator
    kegg_line = kegg_line.rstrip()
    #Splitting line on whitespace
    fields = kegg_line.split()
    if len(fields) > 1:
        kegg = fields[1]
        kegg_ids[kegg] = 1
for kegg_id in kegg_ids:
    print (kegg_id)
    result = subprocess.call("curl http://rest.kegg.jp/link/pathway/"+ kegg_id, stdout = out, stderr = err, shell = True)
