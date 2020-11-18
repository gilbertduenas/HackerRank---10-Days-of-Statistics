# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

import math

mean, std = map(int, input().split())
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print('{:.3f}'.format(cdf(float(input()))))

x, y = map(int, input().split())

print('{:.3f}'.format(cdf(x) - cdf(y)))
