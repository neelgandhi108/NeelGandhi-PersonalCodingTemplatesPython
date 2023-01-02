# Day 1: Interquartile Range

def median(arr):
    N = len(arr)
    if N%2==0:
        med = (arr[int((N-1)*0.5)] + arr[int((N+1)*0.5)])/2
    else:
        med = arr[int(N*0.5)]
    return float(med)

def interQuartile(values, freqs):
    global n
    value_list = []
    for i in range(n):
        for _ in range(freqs[i]):
            value_list.append(values[i])
    value_list.sort()
    n = len(value_list)
    print(round(\
    median(value_list[int((n+1)*0.5):]) - median(value_list[:n//2]), 1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
