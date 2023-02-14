'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    a=len(arr)

    positive_count = 0
    zero_count = 0
    negative_count = 0

    for c in arr:
        if c > 0:
            positive_count +=1
        elif c==0:
            zero_count +=1
        elif c<0:
            negative_count +=1

    print(positive_count/a)
    print(negative_count/a)
    print(zero_count/a)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
