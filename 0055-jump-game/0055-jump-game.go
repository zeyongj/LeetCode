/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
        let len = nums.length;
        let lastGoodIndex = len - 1;
        for (let i = len - 1; i >= 0; i--) {
            if (i + nums[i] >= lastGoodIndex) {
                lastGoodIndex = i;
            }
        }
        return lastGoodIndex == 0;            
};