class Solution:
    def minimumCost(self, A):
        return sum(A) - sum(sorted(A)[-3::-3])