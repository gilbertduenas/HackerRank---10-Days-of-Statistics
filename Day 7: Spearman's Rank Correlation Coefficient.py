# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

# In statistics, Spearman's rank correlation coefficient or Spearman's ρ, named after Charles Spearman and often denoted by the Greek letter rho,
# is a nonparametric measure of rank correlation (statistical dependence between the rankings of two variables). 
# It assesses how well the relationship between two variables can be described using a monotonic function.

# The Spearman correlation between two variables is equal to the Pearson correlation between the rank values of those two variables; 
# while Pearson's correlation assesses linear relationships, Spearman's correlation assesses monotonic relationships (whether linear or not). 
# If there are no repeated data values, a perfect Spearman correlation of +1 or −1 occurs when each of the variables is a perfect monotone function of the other.

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


