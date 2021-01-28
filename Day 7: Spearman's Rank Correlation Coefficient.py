# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

# In statistics, Spearman's rank correlation coefficient or Spearman's ρ, named after Charles Spearman and often denoted by the Greek letter rho,
# is a nonparametric measure of rank correlation (statistical dependence between the rankings of two variables). 
# It assesses how well the relationship between two variables can be described using a monotonic function.

def get_rank(X, n):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]
    
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rx = get_rank(X, n)
ry = get_rank(Y, n)

d = [(rx[i] -ry[i])**2 for i in range(n)]
rxy = 1 - (6 * sum(d)) / (n * (n*n - 1))

print('%.3f' % rxy)

