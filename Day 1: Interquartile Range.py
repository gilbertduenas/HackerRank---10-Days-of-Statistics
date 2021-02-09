# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Interquartile ranges are good for showing how spread out your data is.
# Use this in conjunction with median and total range to see how the data clusters around the mean.

# Unlike total range, the interquartile range has a breakdown point of 25%, and is thus often preferred to the total range.

# The first quartile (Q1) is defined as the middle number between the smallest number (minimum) and the median of the data set. 
# It is also known as the lower or 25th empirical quartile, as 25% of the data is below this point.

# The second quartile (Q2) is the median of a data set; thus 50% of the data lies below this point.
# The third quartile (Q3) is the middle value between the median and the highest value (maximum) of the data set. 
# It is known as the upper or 75th empirical quartile, as 75% of the data lies below this point.

import statistics as stat

n = int(input())
d = list(map(int, input().split()))
f = list(map(int, input().split()))

s = []
N = sum(f)

for i in range(n):
    s += [d[i]] * f[i]
    
s.sort()

if n%2 != 0:
    q1 = stat.median(s[:N//2])
    q3 = stat.median(s[N//2+1:])
    
else:
    q1 = stat.median(s[:N//2])
    q3 = stat.median(s[N//2:])

ir = round(float(q3-q1), 1)

print(ir)

