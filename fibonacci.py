#!usr/bin/env python3
#Fibonacci.py

import sys

def population(n,k):
    sum1 = 0
    mature = 0
    unmature = 0
    maturem = 0
    for i in range(0,n):
        if i == 0:
            sum1 = 1
        elif i == 1:
            sum1 = 1
            mature = 1
        else:
            sum1 = mature + (mature*k) + unmature
            maturem = mature
            mature = unmature + mature
            unmature = maturem * k
    return(sum1)
if __name__ == "__main__":
    argv_count = len(sys.argv) - 1
    if argv_count < 2:
        raise Exception("This script requires 2 arguments: ")
    n = int(sys.argv[1])                                                                                                                                                                                                           
    k = int(sys.argv[2])
    if n > 1000 or k > 1000:                                                                                                                                                                                                                            raise Exception("Population size and Days length should be less then 1000")
    # Passing argument along with function to get population growth on a given day
    populn = population(n, k)
    print("{}".format(populn))
    
