class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])  # path compression
        return self.root[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x==y: return 
        if y > x:
            self.root[y]=x
        else:
            self.root[x]=y
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        G=UnionFind(26)
        n, m=len(s1), len(baseStr)
        for i in range(n):
            G.Union(ord(s1[i])-97, ord(s2[i])-97)
        ans=""
        for x in baseStr:
            ans+=(chr(G.Find(ord(x)-97)+97))
        return ans
        