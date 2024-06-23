class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def mss(arr):
            m, c = 0, 0
            for i in range(len(arr)):
                c += arr[i]
                m = max(m,c)
                if c < 0:
                    c = 0
            return m
        
        MOD = 1000000007
        if k == 1:
            return mss(arr) % MOD
        else:
            p = arr * 2
            m = mss(p)
            o = m+((k-2) * sum(arr))
            return m % MOD if sum(arr) < 0 else o % MOD        