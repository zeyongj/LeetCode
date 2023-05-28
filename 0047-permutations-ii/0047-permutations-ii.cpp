#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        permuteUnique(nums, 0, result);
        return result;
    }

private:
    void permuteUnique(vector<int> nums, int start, vector<vector<int>>& result) {
        if (start == nums.size()) {
            result.push_back(nums);
            return;
        }

        for (int i = start; i < nums.size(); ++i) {
            if (i != start && nums[i] == nums[start]) {
                continue;  // skip duplicates
            }
            swap(nums[start], nums[i]);
            permuteUnique(nums, start + 1, result);
        }
    }
};
