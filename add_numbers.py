#!/usr/bin/env python
#Add_numbers.py

#initialize 2 variables
total=0
total2=0

#Iterate over a range of values
for num in range (1,10):
    #Add num to total and assign to total
    total=total+num
    #Shortcut for the same in one step
    total2 += num

print (total)
print (total2)
