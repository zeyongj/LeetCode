class Solution:
    def minFlips(self, A):
        R, C = len(A), len(A[0])
        base = 0
        for r in range(R // 2):
            for c in range(C // 2):
                cur = A[r][c] + A[r][~c] + A[~r][c] + A[~r][~c]
                base += min(cur, 4 - cur)

        count = [0, 0, 0]
        if R % 2:
            for c in range(C // 2):
                count[A[R // 2][c] + A[R // 2][~c]] += 1
        if C % 2:
            for r in range(R // 2):
                count[A[r][C // 2] + A[~r][C // 2]] += 1

        extra = count[1]
        if count[2] % 2 and not count[1]:
            extra += 2

        if R % 2 and C % 2:
            extra += A[R // 2][C // 2]

        return base + extra