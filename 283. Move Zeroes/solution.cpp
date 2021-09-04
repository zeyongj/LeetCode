class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int cur = 0;
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            if (nums[i] != 0) {
                nums[cur] = nums[i];
                cur ++;
            }
        }
        for (int i = cur; i < size; i++) 
            nums[i] = 0;
    }
};
