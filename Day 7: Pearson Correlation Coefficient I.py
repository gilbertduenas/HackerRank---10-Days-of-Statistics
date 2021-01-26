# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

# Pearson’s correlation coefficient is the test statistics that measures the statistical relationship, or association, between two continuous variables.  
# It is known as the best method of measuring the association between variables of interest because it is based on the method of covariance.  
# It gives information about the magnitude of the association, or correlation, as well as the direction of the relationship.

N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

mu_x = sum(X) / N
mu_y = sum(Y) / N

stdv_x = (sum([(i - mu_x)**2 for i in X]) / N)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in Y]) / N)**0.5

covariance = sum([(X[i] - mu_x) * (Y[i] -mu_y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))
