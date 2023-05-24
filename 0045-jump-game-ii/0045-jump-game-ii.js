/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let n = nums.length;
    let dp = new Array(n).fill(Number.MAX_SAFE_INTEGER);
    dp[n-1] = 0;
    for(let i=n-2; i>=0; i--) {
        let steps = Math.min(n-1, i + nums[i]);
        for(let j=i+1; j<=steps; j++) {
            if(dp[j] != Number.MAX_SAFE_INTEGER) {
                dp[i] = Math.min(dp[i], dp[j] + 1);
            }
        }
    }
    return dp[0];
};
