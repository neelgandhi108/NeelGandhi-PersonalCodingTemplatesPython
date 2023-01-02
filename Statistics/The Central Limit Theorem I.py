# Day 6: The Central Limit Theorem I
import math

# read inputs
max_ = int(input())
box = int(input())
mu = int(input())
std = int(input())

# cdf: normal distribution
def norm(x, mean, std):
    return ((1 + math.erf((x - mean)/(math.sqrt(2)*std)))*0.5)

mu_ = box*mu
std_ = math.sqrt(box)*std

print(round(norm(max_, mu_, std_), 4))
