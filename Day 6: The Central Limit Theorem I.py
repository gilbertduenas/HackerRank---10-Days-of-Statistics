# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

# The central limit theorem (CLT) states that, for a large enough sample (N), 
# the distribution of the sample mean will approach normal distribution. 
# This holds for a sample of independent random variables from any distribution with a finite standard deviation.

from math import erf,sqrt

m = int(input())
n = int(input())
mean = int(input())
std = int(input())

std = std/sqrt(n)
y = m/n

cdf = lambda x: 0.5 * (1 + erf((x-mean)/(std*sqrt(2))))

print(round(cdf(y),4))

