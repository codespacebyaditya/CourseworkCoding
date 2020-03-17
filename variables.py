#!/usr/bin/env python
#variables.py
#A variable containing a string
name = 'Aditya Singh'

#A variable with an integer
age = 21

#A list of strings 
names = ["Aditya Singh", "Surya S", "Arushi Sharma", "Chinmayee Sharma"]

#A list of numbers 
numbers = [15.5, 25.6, 50, 500]

#A dictionary of names and ages
ages = {'Aditya':21, 'Surya':22, 'Random':32}

#Print the values of the variables
print (name)
print (age)
print (names)
print (numbers)
print (numbers)
print (ages)

#Type assigned by python to the variables
print (type(name))
print (type(age))
print (type(names))
print (type (numbers))
print (type(ages))

#Iterate over names in a for loop
for name in names:
    print (name)
    print (type(name))

