/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number}
 */
var longestSubarray = function(nums, limit) {
    let increase = [];
    let decrease = [];
    let max = 0;
    let left = 0;
    
    for (let i = 0; i < nums.length; i++) {
        while (increase.length && nums[i] < increase[increase.length - 1]) {
            increase.pop();
        }
        increase.push(nums[i]);
        
        while (decrease.length && nums[i] > decrease[decrease.length - 1]) {
            decrease.pop();
        }
        decrease.push(nums[i]);
        
        while (decrease[0] - increase[0] > limit) {
            if (nums[left] === decrease[0]) {
                decrease.shift();
            }
            if (nums[left] === increase[0]) {
                increase.shift();
            }
            left++;
        }
        
        max = Math.max(max, i - left + 1);
    }
    
    return max;
};