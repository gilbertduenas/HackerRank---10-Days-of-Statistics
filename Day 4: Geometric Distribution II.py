# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

frac = input().split(' ')
n = int(input())

p = int(frac[0])/int(frac[1])
q = 1 - p
prob = 1 - q**n

print(round(prob,3))
