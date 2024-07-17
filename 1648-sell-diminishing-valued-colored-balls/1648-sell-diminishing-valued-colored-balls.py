class Solution:
    def maxProfit(self, A, O):
        nsum = lambda n : (n * (n + 1)) // 2
        A.sort(reverse = True)
        A.append(0)
        ans, mod = 0, 10 ** 9 + 7
        for i in range(len(A) - 1):
            if (i + 1) * (A[i] - A[i + 1]) > O:
                k, l = O // (i + 1), O % (i + 1)
                return (ans + (i + 1) * (nsum(A[i]) - nsum(A[i] - k)) + l * (A[i] - k)) % mod
            ans = (ans + (i + 1) * (nsum(A[i]) - nsum(A[i + 1]))) % mod
            O -= (i + 1) * (A[i] - A[i + 1])
        return ans