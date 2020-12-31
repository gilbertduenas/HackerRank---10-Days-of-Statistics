# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

# In probability theory and statistics, the binomial distribution with parameters n and p
# is the discrete probability distribution of the number of successes in a sequence of n independent experiments, 
# each asking a yes–no question, and each with its own Boolean-valued outcome: 
# success (with probability p) or failure (with probability q = 1 − p).

def fact(n):
    return 1 if n == 0 else n * fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))

print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))

