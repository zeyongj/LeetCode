class Solution:
    def constructArray(self, n, k):
        dr, diff = 1, k
        result = list(range(1, n-k+1))
        for i in range(k):
            result.append(result[-1] + dr*diff)
            dr *= -1
            diff -= 1      
        return result