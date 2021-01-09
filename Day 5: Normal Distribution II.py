# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

# In probability theory, a normal distribution is a type of continuous probability distribution for a real-valued random variable. 

# The normal distribution is a probability distribution. 
# It is also called Gaussian distribution because it was first discovered by Carl Friedrich Gauss.
# The normal distribution is a continuous probability distribution that is very important in many fields of science.

import math

# Take the mean and standard deviation and calculate the normal distribution.
mean, std = map(int, input().split())
a = int(input())
b = int(input())

# cumulative distribution function is the probability that X will take a value less than or equal to x.
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round((1-cdf(a))*100,2))
print(round((1-cdf(b))*100,2))
print(round((cdf(b))*100,2))

