# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

# The central limit theorem (CLT) states that, for a large enough sample (N), 
# the distribution of the sample mean will approach normal distribution. 
# This holds for a sample of independent random variables from any distribution with a finite standard deviation.

# When independent random variables are added, their properly normalized sum tends toward a normal distribution 
# (informally a bell curve) even if the original variables themselves are not normally distributed.

mu, sigma = 500, 80

muS, sigmaS = mu, sigma/(100**0.5)

A = mu - (1.96*sigmaS)
B = mu + (1.96*sigmaS)

print(round(A,2))
print(round(B,2))

