# Day 6: The Central Limit Theorem II
import math

# read all inputs
max_tic = int(input())
tic = int(input())
mu = float(input())
std = float(input())

# CDF: normal distribution
def norm(x, mean, std):
    return ((1 + math.erf((x - mean)/(math.sqrt(2)*std)))*0.5)

mu_ = tic * mu
std_ = math.sqrt(tic) * std

print(round(norm(max_tic, mu_, std_), 4))
