# Day 4: Geometric Distribution I
p1, p2 = map(int, input().split())
p0 = int(input())

p = p1/p2

def geo(n, p):
    return round((p*((1-p)**(n-1))), 3)

print(geo(p0, p))