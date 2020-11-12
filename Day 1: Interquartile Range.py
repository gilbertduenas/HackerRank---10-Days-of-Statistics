# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

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
