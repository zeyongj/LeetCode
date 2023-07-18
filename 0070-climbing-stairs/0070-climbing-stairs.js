/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
        if (n <= 2) return n;
        
        var oneStepBefore = 2;
        var twoStepsBefore = 1;
        var allWays = 0;
        
        for (var i = 2; i < n; i++) {
            allWays = oneStepBefore + twoStepsBefore;
            twoStepsBefore = oneStepBefore;
            oneStepBefore = allWays;
        }
        return allWays;    
};