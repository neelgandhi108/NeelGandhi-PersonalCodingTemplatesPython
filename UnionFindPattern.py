Union Find
Union Find is a useful algorithm for graph

DSU for integers

class DSU:
    def __init__(self, N):
        self.par = list(range(N))

    def find(self, x): # Find Parent
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: # If parents are equal, return False
            return False
        self.par[yr] = xr # Give y node parent of x
        return True # return True if union occured
DSU for strings

class DSU:
    def __init__(self):
        self.par = {}

    def find(self, x):
        if x != self.par.setdefault(x, x):
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        self.par[yr] = xr
DSU with union by rank

class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True