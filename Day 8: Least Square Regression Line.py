# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

# The Least Squares Regression Line is the line that makes the vertical distance from the data points to the regression line as small as possible. 
# It's called a “least squares” because the best line of fit is one that minimizes the variance (the sum of squares of the errors).

n = 5
xy = [map(int, input().split()) for _ in range(n)]

sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (n * sxy - sx * sy) / (n * sx2 - sx**2)
a = (sy / n) - b * (sx / n)

print('{:.3f}'.format(a + b * 80))


