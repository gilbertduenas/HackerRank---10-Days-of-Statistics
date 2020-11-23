# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

l = []

N = int(input())
X = [int(x) for x in input().split()]
W = [int(w) for w in input().split()]

for i in range(0, N):
    w = X[i] * W[i]
    l.append(w)

m = round(float(sum(l)/sum(W)), 1)

print(m)

