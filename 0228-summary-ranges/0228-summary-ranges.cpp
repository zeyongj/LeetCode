#include <vector>
#include <string>

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> result;
        if (nums.empty()) {
            return result;
        }

        for (int i = 0; i < nums.size(); ++i) {
            int start = nums[i];

            while (i + 1 < nums.size() && nums[i] + 1 == nums[i + 1]) {
                ++i;
            }

            if (start != nums[i]) {
                result.push_back(to_string(start) + "->" + to_string(nums[i]));
            } else {
                result.push_back(to_string(start));
            }
        }

        return result;
    }
};
