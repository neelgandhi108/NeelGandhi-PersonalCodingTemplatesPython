# Day 1: Standard Deviation

def mean(arr):
    global n
    sum_ = 0
    for i in range(n):
        sum_ += arr[i]
    return n, sum_/n

def stdDev(arr):
    n, mean_ = mean(arr)
    std = 0
    for i in range(n):
        std += ((mean_ - arr[i])**2)
    print((std/n)**0.5)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
