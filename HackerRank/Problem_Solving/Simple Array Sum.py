'''
Given an array of integers, find the sum of its elements.
'''
#!/bin/python3
lst = int(input())
ar = list(map(int, input().rstrip().split()))
#ar = [1, 34, 6, 879]
en = enumerate(ar)
sum = 0
for idx, value in en:
    sum += value

print(sum)
