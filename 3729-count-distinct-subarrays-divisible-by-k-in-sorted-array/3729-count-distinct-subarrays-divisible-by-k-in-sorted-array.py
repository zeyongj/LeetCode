class Solution:
    def numGoodSubarrays(self, A: List[int], k: int) -> int:
        count = Counter([0])
        res = pre = 0
        for a in A:
            pre = (pre + a) % k
            res += count[pre]
            count[pre] += 1
        for a, it in groupby(A):
            l = len(list(it))
            for ll in range(1, l):
                if ll * a % k == 0:
                    res -= l - ll
        return res