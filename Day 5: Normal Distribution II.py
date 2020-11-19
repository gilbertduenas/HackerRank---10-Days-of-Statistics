# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

import math

mean, std = map(int, input().split())
a = int(input())
b = int(input())
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round((1-cdf(a))*100,2))
print(round((1-cdf(b))*100,2))
print(round((cdf(b))*100,2))