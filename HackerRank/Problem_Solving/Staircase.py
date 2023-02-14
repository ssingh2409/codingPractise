'''
Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        space = ' ' * ((n-i)-1)
        star = '#' * (i+1)
        print(space+star)
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
