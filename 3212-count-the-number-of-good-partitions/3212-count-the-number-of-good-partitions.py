class Solution:
    def numberOfGoodPartitions(self, A: List[int]) -> int:
        last = {a: i for i,a in enumerate(A)}
        res = 1
        mod = 10 ** 9 + 7
        j = 0
        for i,a in enumerate(A):
            if i > j:
                res = res * 2 % mod
            j = max(j, last[a])
        return res   