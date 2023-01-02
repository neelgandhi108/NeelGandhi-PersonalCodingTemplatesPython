# Day 5: Poisson Distribution I
import math
mean = float(input())
X = int(input())

def fact(x):
    if x == 0:
        n = 1
    else:
        n = 1
        for i in range(1, x+1):
            n *= i
    return n

def pois(X, mean):
    return round(((mean**X)*(math.exp(-mean)))/fact(X), 3)

print(pois(X, mean))
