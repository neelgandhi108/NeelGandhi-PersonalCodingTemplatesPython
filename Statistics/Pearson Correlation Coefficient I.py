# Day 7: Pearson Correlation Coefficient I
import math

# Read inputs 
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

# check n == len(X) == len(Y)

# mean
def mean(a):
    return sum(a)/len(a)

# standard deviation
def std(a):
    global n
    mu = mean(a)
    sum_ = 0.0
    for i in range(n):
        sum_ += ((a[i] - mu)**2)
    return math.sqrt(sum_/n)

# corr(X, Y)
def corr(arr1, arr2):
    global n
    mean1 = mean(arr1)
    mean2 = mean(arr2)
    conv = 0.0
    for i in range(n):
        conv += (arr1[i] - mean1) * (arr2[i] - mean2)
    print(round(conv/(n*std(arr1)*std(arr2)), 3))

corr(X, Y)
