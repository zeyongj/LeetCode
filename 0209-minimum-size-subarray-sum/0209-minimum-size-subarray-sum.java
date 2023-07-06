class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, right = 0;
        int sum = 0;
        int min_len = Integer.MAX_VALUE;
        
        while(right < nums.length){
            sum += nums[right];
            
            while(sum >= target){
                min_len = Math.min(min_len, right - left + 1);
                sum -= nums[left];
                left++;
            }
            right++;
        }
        return (min_len != Integer.MAX_VALUE) ? min_len : 0;        
    }
}