class Solution:
    def haveConflict(self, e1, e2):
        return max(e1[0],e2[0]) <= min(e1[1],e2[1])