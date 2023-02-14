'''
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
'''
x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])

while True:
    s1 = x1 + v1
    s2 = x2 + v2
    if s1 == s2:
        print('YES')
        break
    elif v1 <= v2 and x1 < x2:
        print('NO')
        break
    elif v1 >= v2 and x1 > x2:
        print('NO')
        break
    else:
        x1 += v1
        x2 += v2
