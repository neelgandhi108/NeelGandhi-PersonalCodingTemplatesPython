# Day 0: Mean, Median, and Mode
N = int(input())
sample = sorted(list(map(float, input().strip().split())))
if N == len(sample):
    # mean
    sum_ = 0
    for i in sample:
        sum_ += i
    mean = sum_/N
    # median
    if N%2 == 0:
        median = (sample[int(N/2-0.5)] + sample[int(N/2+0.5)])/2
    else:
        median = sample[int(N/2+0.5)]
    # mode
    mode = []
    count = {}
    for i in sample:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key in count.keys():
        if count[key] == max(count.values()):
            mode.append(key)
    
    print(round(mean, 1))
    print(round(median, 1))
    print(mode[0])