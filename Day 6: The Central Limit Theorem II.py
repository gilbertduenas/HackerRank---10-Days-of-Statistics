# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

# The central limit theorem (CLT) states that, for a large enough sample (N), 
# the distribution of the sample mean will approach normal distribution. 
# This holds for a sample of independent random variables from any distribution with a finite standard deviation.

# The central limit theorem states that if you have a population with mean μ and standard deviation σ 
# and take sufficiently large random samples from the population with replacement, 
# then the distribution of the sample means will be approximately normally distributed.

# When independent random variables are added, their properly normalized sum tends toward a normal distribution 
# (informally a bell curve) even if the original variables themselves are not normally distributed.

from math import erf,sqrt

m = int(input())
n = int(input())
mean = float(input())
std = float(input())

std = std/sqrt(n)
y = m/n

cdf = lambda x: 0.5 * (1 + erf((x-mean)/(std*sqrt(2))))

print(round(cdf(y),4))
