# Day 5: Normal Distribution I
import math

# read input
mean, std = map(float, input().split())
X1 = float(input())
X2, X3 = map(float, input().split())

'''
# pdf: normal distribution
def norm(x, mean, std):
    con1 = math.exp(-((x - mean)**2)/(2*(std**2)))
    return con1/(std*math.sqrt(2*math.pi))
'''

# cdf: normal distribution
def norm(x, mean, std):
    return ((1 + math.erf((x - mean)/(math.sqrt(2)*std)))*0.5)

# Q01
print(round(norm(X1, mean, std), 3))

# Q02
print(round((norm(X3, mean, std) - norm(X2, mean, std)), 3))
