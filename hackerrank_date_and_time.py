import math
import os
import random
import re
import sys
from datetime import datetime

month_map = {'Jan' : 1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_since_epoch(y, m, d):
    days = d
    for year in range(1970, y):
        days += 366 if is_leap(year) else 365
    for i in range(m-1):
        days += month_days[i]
        if i == 1 and is_leap(y):
            days += 1
    return days

def parse_timestamp(t):
    t = t.split()
    day = int(t[1])
    month = month_map[t[2]]
    year = int(t[3])
    h, m, s = map(int, t[4].split(':'))
    offset = t[5]
    
    sign = -1 if offset[0] == '-' else 1
    offset_hours = int(offset[1:3])
    offset_min = int(offset[3:])
    offset_seconds = sign * (offset_hours * 3600 + offset_min * 60)
    
    total_days = days_since_epoch(year, month, day)
    total_seconds = total_days * 86400 + h * 3600 + m * 60 + s - offset_seconds
    
    return total_seconds

def time_delta(t1, t2):
    t1 = parse_timestamp(t1)
    t2 = parse_timestamp(t2)
    return(str(abs(t1-t2)))
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
