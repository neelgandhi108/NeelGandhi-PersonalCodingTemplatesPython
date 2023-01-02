# Day 4: Geometric Distribution II
p1, p2 = map(int, input().split())
p0 = int(input())

p = p1/p2

def geo(n, p):
    return round(sum([(p*((1-p)**(i-1))) for i in range(1, n+1)]), 3)

print(geo(p0, p))
