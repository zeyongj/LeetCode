public class Solution {
    public int FirstMissingPositive(int[] nums) {
        int n = nums.Length;

        // First, we segregate positive numbers and non-positive numbers.
        for(int i = 0; i < n; ++i) {
            while(nums[i] > 0 && nums[i] <= n) {
                int correctPos = nums[i] - 1; // Calculate correct position first
                if(nums[correctPos] != nums[i]) {
                    int temp = nums[i];
                    nums[i] = nums[correctPos];
                    nums[correctPos] = temp;
                } else {
                    break;
                }
            }
        }

        // Then, we find the first index where the index+1 doesn't match the number at that index
        for(int i = 0; i < n; ++i) {
            if(nums[i] != i + 1) {
                return i + 1; // As the array is 0-indexed, the first missing positive is i+1
            }
        }

        // If all indices matched, then the first missing positive is the array size+1
        return n + 1;
    }
}
