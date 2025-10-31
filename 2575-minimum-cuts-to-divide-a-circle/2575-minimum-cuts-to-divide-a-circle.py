class Solution:
    def numberOfCuts(self, n) -> int:
        if (n %2 == 1 and n > 1):
            return n
        else:
            return n // 2