#!/usr/bin/env python3

#a function to multiply two numbers and return the product
def multiply(a,b):
    return a * b

#function to print Hello, you!
def hello_name(name="you"):
    return("Hello, {}!".format(name))

#function to return numbers less than 10
def less_than_ten(numlist):
    new_list=[]
    for x in numlist:
        if x<10:
            new_list.append(x)
    return new_list
