# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

import numpy as np
from scipy import stats

s = int(input())
n = list(map(int, input().split()))

# An important property of the mean is that it includes every value in your data set as part of the calculation. 
# In addition, the mean is the only measure of central tendency where the sum of the deviations of each value from the mean is always zero.

# The mean has one main disadvantage: it is particularly susceptible to the influence of outliers. 
# These are values that are unusual compared to the rest of the data set by being especially small or large in numerical value. 
print(np.mean(n))

# The median is less affected by outliers and skewed data. 

# Data should be ordinal.
print(np.median(n))

# Mode is good for categorical data and determining the most common category.
print(int(stats.mode(n)[0]))
