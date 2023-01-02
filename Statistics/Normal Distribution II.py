# Day 5: Normal Distribution II
import math

mu, std = map(float, input().split())
X1 = float(input())
X2 = float(input())

# cdf: normal distribution
def norm(x, mean, std):
    return ((1 + math.erf((x - mean)/(math.sqrt(2)*std)))*0.5)*100

# X > X1
print(round(100 - norm(X1, mu, std), 2))

# X >= X2
print(round(100 - norm(X2, mu, std), 2))

# X < X2
print(round(norm(X2, mu, std), 2))
