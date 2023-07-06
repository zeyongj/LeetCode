public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        int left = 0, right = 0;
        int sum = 0;
        int min_len = Int32.MaxValue;
        
        while(right < nums.Length){
            sum += nums[right];
            
            while(sum >= target){
                min_len = Math.Min(min_len, right - left + 1);
                sum -= nums[left];
                left++;
            }
            right++;
        }
        return (min_len != Int32.MaxValue) ? min_len : 0;                
    }
}