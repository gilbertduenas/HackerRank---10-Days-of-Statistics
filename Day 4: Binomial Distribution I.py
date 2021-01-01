# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

# In probability theory and statistics, the binomial distribution with parameters n and p
# is the discrete probability distribution of the number of successes in a sequence of n independent experiments, 
# each asking a yes–no question, and each with its own Boolean-valued outcome: 
# success (with probability p) or failure (with probability q = 1 − p).

import math

def bi_dist(x, n, p):
    b = (math.factorial(n) / (math.factorial(x) * math.factorial(n-x))) * (p**x) * ((1-p)**(n-x))
    
    return(b)

b, p, n = 0, 1.09/2.09, 6

for i in range(3,7):
    b += bi_dist(i, n, p)   

print("%.3f" %b)
