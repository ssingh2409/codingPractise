'''
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.
'''
#!/bin/python3
import math
import os
import random
import re
import sys

def breakingRecords(scores):
    for i, val in enumerate(scores):
        if i == 0:
            high, low, high_brk, low_brk = val, val, 0, 0
        else:
            if val > high:
                high = val
                high_brk += 1
            elif val < low:
                low = val
                low_brk += 1
    
    return [high_brk, low_brk]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
