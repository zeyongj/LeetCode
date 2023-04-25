/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length === 0) {
            return 0;
        }

        let uniqueIndex = 0;
        for (let i = 1; i < nums.length; i++) {
            if (nums[i] !== nums[uniqueIndex]) {
                uniqueIndex++;
                nums[uniqueIndex] = nums[i];
            }
        }

        return uniqueIndex + 1;
};