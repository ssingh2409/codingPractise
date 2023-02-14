'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals
'''
n = int(input().strip())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

sum_left = 0
sum_right = 0
size = len(arr[0])

for i in range(0,size):
    sum_left += arr[i][i]
    sum_right += arr[i][size - 1 - i]

sm = abs(sum_left - sum_right)
print(sm)
