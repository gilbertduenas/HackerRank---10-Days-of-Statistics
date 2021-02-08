# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

# This is a mean where some values contribute more than others.

# Useful when calculating a theoretically expected outcome where each outcome has a different probability of occurring, 
# which is the key feature that distinguishes the weighted mean from the arithmetic mean.

l = []

N = int(input())
X = [int(x) for x in input().split()]
W = [int(w) for w in input().split()]

for i in range(0, N):
    w = X[i] * W[i]
    l.append(w)

m = round(float(sum(l)/sum(W)), 1)

print(m)

