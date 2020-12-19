# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# This is the amount of variation or dispersion of a set of values.

n = int(input().strip())
X = [int(x) for x in input().strip().split()]

mean = sum(X) / n
variance = sum([((x - mean) ** 2) for x in X]) / n
stddev = variance ** 0.5

print('{0:0.1f}'.format(stddev))
