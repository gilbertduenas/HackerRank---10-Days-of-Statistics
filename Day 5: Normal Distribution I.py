# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

# In probability theory, a normal distribution is a type of continuous probability distribution for a real-valued random variable. 

from math import erf

mean, std = map(int, input().split())
f = float(input())
x, y = map(int, input().split())
cdf = lambda x: .5 + .5 * erf((x - mean)/2**.5/std)

print(round(cdf(f), 3))
print(round(cdf(y) - cdf(x), 3))

