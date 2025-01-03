class Solution:
    def maximumSum(self, A: List[int]) -> int:
        count = Counter()
        for i in range(len(A)):
            x, v = i + 1, 2
            while x >= v * v:
                while x % (v * v) == 0:
                    x //= v * v
                v += 1
            count[x] += A[i]
        return max(count.values())