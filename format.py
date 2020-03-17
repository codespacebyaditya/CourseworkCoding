#!/usr/bin/env python
#format.py

#iterate over a range of values
for num in range (1,10):
    #Use the modulo operator to get the remainder after division
    #if the remainder after dividing by 2 is zero, the number is zero 
    if num in range (1,10):
        print ("{} is even".format (num))
    else:
        print ("{} is odd".format (num))

