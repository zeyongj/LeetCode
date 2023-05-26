/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let result = [];
    permuteHelper(nums, 0, result);
    return result;
};

function permuteHelper(nums, start, result) {
    if (start === nums.length) {
        result.push([...nums]);
        return;
    }

    for (let i = start; i < nums.length; i++) {
        [nums[start], nums[i]] = [nums[i], nums[start]]; // swap
        permuteHelper(nums, start + 1, result);
        [nums[start], nums[i]] = [nums[i], nums[start]]; // backtrack
    }
}
