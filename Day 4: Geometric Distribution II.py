# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

# A negative binomial experiment is a statistical experiment that has the following properties:

# The experiment consists of N repeated trials.
# The trials are independent.
# The outcome of each trial is either success (s) or failure (f).
# P(s) is the same for every trial.
# The experiment continues until X successes are observed.

frac = input().split(' ')
n = int(input())

p = int(frac[0])/int(frac[1])
q = 1 - p
prob = 1 - q**n

print(round(prob,3))

