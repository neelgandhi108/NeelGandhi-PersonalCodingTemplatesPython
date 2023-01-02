# Day 1: Quartiles

import os

def medium(arr):
    n = len(arr)
    if n%2 == 0:
        Q =  (arr[int((n-1)*0.5)] + arr[int((n+1)*0.5)])/2
    else:
        Q =  arr[int(n*0.5)]
    if Q - int(Q) == 0:
        return int(Q)
    else:
        return Q
    
def quartiles(arr):
    n = len(arr)

    Q2 = medium(arr)
    Q1 = medium(arr[:n//2])
    Q3 = medium(arr[int(n/2+0.5):])
        
    return Q1, Q2, Q3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(sorted(map(int, input().rstrip().split())))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
