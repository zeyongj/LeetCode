class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        
        n = len(s)
        if k == 1 or k == n: return (s == t)|(k == n)

        m = n // k
        d = defaultdict(int)

        for i in range(0, n, m): 
            d[s[i: i + m]]+= 1

        for i in range(0, n, m):
            tt = t[i: i + m]
            d[tt]-= 1
            if d[tt] < 0: return False
            
        return True