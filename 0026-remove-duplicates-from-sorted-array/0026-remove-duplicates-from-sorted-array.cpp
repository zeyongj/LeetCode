#include <vector>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        int size = nums.size();
        if (size == 0) {
            return 0;
        }

        int uniqueIndex = 0;
        for (int i = 1; i < size; i++) {
            if (nums[i] != nums[uniqueIndex]) {
                uniqueIndex++;
                nums[uniqueIndex] = nums[i];
            }
        }

        return uniqueIndex + 1;
    }
};
