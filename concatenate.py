#!/usr/bin/env python
#concatenate.py

#Iterate over a range of values

for num in range (1,10):
    #Use the modulus operator to get the remainder after division 
    #If the remained is zero, the number is even 
    if num%2==0:
        print (str(num)+ ' is even')
    else:
        print (str(num)+ ' is odd')

