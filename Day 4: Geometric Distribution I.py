# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

prob = [float(i) for i in input().split(' ')]
ins = int(input())

res = pow(1-float(prob[0]/prob[1]),ins-1) * float(prob[0]/prob[1])

print("{:.3f}".format(res))
