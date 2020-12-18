# https://www.hackerrank.com/challenges/s10-quartiles/problem

# In statistics, a quartile is a type of quantile which divides the number of data points into four parts, or quarters, of more-or-less equal size. 
# The data must be ordered from smallest to largest to compute quartiles; as such, quartiles are a form of order statistic. 
# The three main quartiles are as follows:

# The first quartile (Q1) is defined as the middle number between the smallest number (minimum) and the median of the data set. 
# It is also known as the lower or 25th empirical quartile, as 25% of the data is below this point.

# The second quartile (Q2) is the median of a data set; thus 50% of the data lies below this point.

# The third quartile (Q3) is the middle value between the median and the highest value (maximum) of the data set. 
# It is known as the upper or 75th empirical quartile, as 75% of the data lies below this point.

from statistics import median

n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
t=int(len(arr)/2)

if len(arr)%2==0:
    L=arr[:t]
    U=arr[t:]

else:
    L=arr[:t]
    U=arr[t+1:]
    
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))

