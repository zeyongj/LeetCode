class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        size = len(A)

        for i in range(size - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0