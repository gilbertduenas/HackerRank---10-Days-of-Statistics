# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# This is the amount of variation or dispersion of a set of values.

# A low standard deviation indicates that the values tend to be close to the mean (also called the expected value) of the set, 
# while a high standard deviation indicates that the values are spread out over a wider range.

n = int(input().strip())
X = [int(x) for x in input().strip().split()]

mean = sum(X) / n
variance = sum([((x - mean) ** 2) for x in X]) / n
stddev = variance ** 0.5

print('{0:0.1f}'.format(stddev))
