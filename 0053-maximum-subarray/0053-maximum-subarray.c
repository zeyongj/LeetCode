int maxSubArray(int* nums, int numsSize){
        int max_sum = nums[0];
        int current_sum = nums[0];

        for(int i = 1; i < numsSize; i++){
            current_sum = fmax(nums[i], current_sum + nums[i]);
            max_sum = fmax(max_sum, current_sum);
        }

        return max_sum;
}