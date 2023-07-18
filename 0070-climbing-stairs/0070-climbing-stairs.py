class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n

        oneStepBefore = 2
        twoStepsBefore = 1
        allWays = 0
        
        for i in range(2,n):
            allWays = oneStepBefore + twoStepsBefore
            twoStepsBefore = oneStepBefore
            oneStepBefore = allWays

        return allWays