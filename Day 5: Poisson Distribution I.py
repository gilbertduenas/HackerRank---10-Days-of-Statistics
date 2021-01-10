# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

# This is a discrete probability distribution that expresses the probability of a given number of events occurring 
# in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event.
# The Poisson distribution can also be used for the number of events in other specified intervals such as distance, area or volume.

from math import factorial, exp

m = float(input())
x = int(input())

p = ((miu ** x) * exp(-m)) / factorial(x)

print("%.3f" %p)

