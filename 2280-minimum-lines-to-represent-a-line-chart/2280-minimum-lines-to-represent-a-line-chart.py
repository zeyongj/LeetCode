class Solution:
    def minimumLines(self, A: List[List[int]]) -> int:
        n = len(A)
        res = n - 1
        A.sort()
        for i in range(1, n - 1):
            a, b, c = A[i-1], A[i], A[i+1]
            if (b[0] - a[0]) * (c[1] - b[1]) == (c[0] - b[0]) * (b[1] - a[1]):
                res -= 1
        return res