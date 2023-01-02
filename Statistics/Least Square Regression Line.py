# Day 8: Least Square Regression Line
from math import sqrt

# Read inputs into array
n = 5
X, Y = list(), list()
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

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
    return sqrt(sum_/n)

# corr(X, Y)
def corr(arr1, arr2):
    global n
    mean1 = mean(arr1)
    mean2 = mean(arr2)
    conv = 0.0
    for i in range(n):
        conv += (arr1[i] - mean1) * (arr2[i] - mean2)
    return conv/(n*std(arr1)*std(arr2))

# fit the best-fit line using least squares and find the value of y
def liner(X, Y, x1):
    b = corr(X,Y)*(std(Y)/std(X))
    a = mean(Y) - (b*mean(X))
    print(round(a + (b*x1), 3))

liner(X, Y, 80)
