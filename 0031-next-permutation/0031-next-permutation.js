/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    const swap = (nums, i, j) => {
        let temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    const reverse = (nums, start, end) => {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }

    let i = nums.length - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        let j = nums.length - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        swap(nums, i, j);
    }
    reverse(nums, i + 1, nums.length - 1);    
};