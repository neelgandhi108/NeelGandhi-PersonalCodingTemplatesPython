# Day 0: Weighted Mean

def weightedMean(X, W):
    global n
    XW_sum = 0
    W_sum = 0
    for i in range(n):
        XW_sum += X[i] * W[i]
        W_sum += W[i]
    print(round((XW_sum/W_sum), 1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)