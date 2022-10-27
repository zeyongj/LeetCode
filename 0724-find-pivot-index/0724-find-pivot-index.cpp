class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum, left_sum = 0;
        for (int num:nums){
            sum += num;
        }
        for (int i = 0; i < nums.size(); i++){
            if (left_sum == sum - left_sum - nums[i])
                return i;
            else
                left_sum += nums[i];
        }
        return -1;
    }
};