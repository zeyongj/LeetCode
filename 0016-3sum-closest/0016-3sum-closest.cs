using System;

public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        int n = nums.Length;
        Array.Sort(nums);
        int closestSum = nums[0] + nums[1] + nums[2];
        int minDiff = Math.Abs(target - closestSum);

        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                int diff = Math.Abs(target - sum);

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
    }
}
