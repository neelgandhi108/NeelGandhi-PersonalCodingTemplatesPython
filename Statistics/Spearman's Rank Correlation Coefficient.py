# Day 7: Spearman's Rank Correlation Coefficient

# Read inputs
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

# Ranking
def rank(arr):
    return [sorted(arr).index(x)+1 for x in arr]

# Spearman's rank correlation
def corr(arr1, arr2):
    global n
    r_arr1 = rank(arr1)
    r_arr2 = rank(arr2)
    sum_ = 0.0
    for i in range(n):
        sum_ += (r_arr1[i] - r_arr2[i])**2
    print(round(1-((6*sum_)/(n*((n**2)-1))), 3))

corr(X, Y)
