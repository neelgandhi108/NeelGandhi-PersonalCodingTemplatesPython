# Day 4: Binomial Distribution  I
p1, n = map(float, input().split())

# p for boys
gap = 1/(1 + (n/p1))
x = 3
n = 6

def fact(x):
    a = 1
    for i in range(1, x+1):
        a *= i
    return a

def comb(n, r):
    return float(fact(n)/(fact(r)*fact(n-r)))

def bino(x, n, p):
    q = 1 - p
    return (comb(n, x)*(p**x)*(q**(n-x)))

print(round(sum([bino(i, n, gap) for i in range(x, n+1)]), 3))
