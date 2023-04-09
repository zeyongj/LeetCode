/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let n = nums.length;
    nums.sort((a, b) => a - b);
    let closestSum = nums[0] + nums[1] + nums[2];
    let minDiff = Math.abs(target - closestSum);

    for (let i = 0; i < n - 2; i++) {
        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            let sum = nums[i] + nums[left] + nums[right];
            let diff = Math.abs(target - sum);

            if (diff < minDiff) {
                minDiff = diff;
                closestSum = sum;
            }

            if (sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            } else {
                return target; // The sum is equal to the target, so it's the closest.
            }
        }
    }

    return closestSum;
};
