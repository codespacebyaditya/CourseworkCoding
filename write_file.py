#1/usr/bin/env python

#write_file.py
line_to_write= 'random text abcdefghijklmnopqrstuvwxyz'

with open ("out_file.txt",'w') as out:
    #output line 
    out.write(line_to_write)

