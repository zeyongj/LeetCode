public class Solution {
    public int ClimbStairs(int n) {
        if (n <= 2) return n;
        
        int oneStepBefore = 2;
        int twoStepsBefore = 1;
        int allWays = 0;
        
        for (int i = 2; i < n; i++) {
            allWays = oneStepBefore + twoStepsBefore;
            twoStepsBefore = oneStepBefore;
            oneStepBefore = allWays;
        }
        return allWays;        
    }
}