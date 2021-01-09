# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

# In probability theory, a normal distribution is a type of continuous probability distribution for a real-valued random variable. 

# The normal distribution is a probability distribution. 
# It is also called Gaussian distribution because it was first discovered by Carl Friedrich Gauss.
# The normal distribution is a continuous probability distribution that is very important in many fields of science.

# erf is error function
from math import erf

# Take the mean and standard deviation and calculate the normal distribution.
mean, std = map(int, input().split())
f = float(input())
x, y = map(int, input().split())

# cumulative distribution function is the probability that X will take a value less than or equal to x.
cdf = lambda x: .5 + .5 * erf((x - mean)/2**.5/std)

print(round(cdf(f), 3))
print(round(cdf(y) - cdf(x), 3))

