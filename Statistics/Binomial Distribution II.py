# Day 4: Binomial Distribution II
p, n = map(int, input().split())

p /= 100

def fact(x):
    if x == 0:
        a = 1
    else:
        a = 1
        for i in range(1, x+1):
            a *= i
    return a

def comb(n, r):
    return float(fact(n)/(fact(r)*fact(n-r)))

def bino(x, n, p):
    q = 1 - p
    return (comb(n, x)*(p**x)*(q**(n-x)))

def prob(from_, to_):
    print(round(sum([bino(i, n, p) for i in range(from_, to_+1)]), 3))

# no more than 2 rejects
prob(0, 2)

# at least 2 rejects
prob(2, n)

