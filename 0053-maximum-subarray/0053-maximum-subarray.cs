public class Solution {
    public int MaxSubArray(int[] nums) {
        int max_sum = nums[0];
        int current_sum = nums[0];

        for(int i = 1; i < nums.Length; i++){
            current_sum = Math.Max(nums[i], current_sum + nums[i]);
            max_sum = Math.Max(max_sum, current_sum);
        }

        return max_sum;        
    }
}