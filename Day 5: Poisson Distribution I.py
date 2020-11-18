# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

from math import factorial, exp

m = float(input())
x = int(input())

p = ((miu ** x) * exp(-m)) / factorial(x)

print("%.3f" %p)
