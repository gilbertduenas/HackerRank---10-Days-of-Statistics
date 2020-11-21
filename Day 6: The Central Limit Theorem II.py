# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

from math import erf,sqrt

m = int(input())
n = int(input())
mean = float(input())
std = float(input())

std = std/sqrt(n)
y = m/n

cdf = lambda x: 0.5 * (1 + erf((x-mean)/(std*sqrt(2))))

print(round(cdf(y),4))
