'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
'''
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    am_or_pm = s[-2:]
    s = s[:-2]
    hh = int(s[:2])

    if am_or_pm == 'PM' and hh != 12:
        hh += 12
        new_s = str(hh) + s[2:]
    elif am_or_pm == 'AM' and hh == 12:
        new_s = str('00') + s[2:]
    else:
        new_s = s

    return new_s
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
