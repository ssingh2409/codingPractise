'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_min = 0
    sum_max = 0
    arr.sort()
    for num in arr[0:4]:
        sum_min += num

    arr.sort(reverse=True)
    for num in arr[0:4]:
        sum_max += num

    print(sum_min, sum_max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
