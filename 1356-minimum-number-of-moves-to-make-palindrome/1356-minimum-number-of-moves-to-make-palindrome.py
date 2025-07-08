class BIT:
    def __init__(self, n):
        self.sums = [0] * (n+1)
    
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

class Solution:
    def minMovesToMakePalindrome(self, s):
        n = len(s)
        s = [ord(x) - 95 for x in s]
        ans, bit = 0, BIT(n)
        if sum(x % 2 == 1 for x in Counter(s).values()) > 1: return -1

        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)

        B, P = [0] * n, []
        for c, I in idx.items():
            cnt = len(I)
            if cnt % 2:
                B[I[cnt//2]] = n//2 + 1
            for i in range((cnt)//2):
                P += [(I[i], I[~i])]

        for i, (l, r) in enumerate(sorted(P)):
            B[l], B[r] = i + 1, n - i
        
        for i, b in enumerate(B):
            ans += i - bit.query(b)
            bit.update(b, 1)
        
        return ans