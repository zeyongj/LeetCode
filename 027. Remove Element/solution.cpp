class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        if (size == 0)
            return 0;
        int j = 0;
        int k = size  - 1;
        while (j < k) {
            while (j < k && nums[j] != val)
                j++;
            while (j < k && nums[k] == val)
                k--;
            int temp = nums[j];
            nums[j] = nums[k];
            nums[k] = temp;
        }
        if (nums[j] == val)
            return j;
        else
            return ++j;
    }
};
