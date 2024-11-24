class Solution:
    def minOperations(self, k: int) -> int:
        res = k
        for i in range(1, math.ceil(math.sqrt(k)) + 1):
            x = math.ceil(k / i)
            res = min(res, x + math.ceil(k / x) - 2)
            res = min(res, i + math.ceil(k / i) - 2)
        return res