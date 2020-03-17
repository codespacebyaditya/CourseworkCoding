#!/usr/bin/env python3
import sys
def hello_name (str="you"):
    print("Hello, {}!".format(str))

if __name__== "__main__":
    argvcount=len(sys.argv) - 1
    if argvcount < 1:
        hello_name()
    else:
        hello_name(sys.argv[1])
