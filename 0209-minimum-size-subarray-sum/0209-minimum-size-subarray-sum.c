int minSubArrayLen(int target, int* nums, int numsSize){
        int left = 0, right = 0;
        int sum = 0;
        int min_len = INT_MAX;
        
        while(right < numsSize){
            sum += nums[right];
            
            while(sum >= target){
                min_len = fmin(min_len, right - left + 1);
                sum -= nums[left];
                left++;
            }
            right++;
        }
        return (min_len != INT_MAX) ? min_len : 0;
}