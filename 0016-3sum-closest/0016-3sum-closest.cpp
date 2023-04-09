#include <algorithm>
#include <vector>
#include <limits>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int closest_sum = nums[0] + nums[1] + nums[2];
        int min_diff = abs(target - closest_sum);
        
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                int diff = abs(target - sum);
                
                if (diff < min_diff) {
                    min_diff = diff;
                    closest_sum = sum;
                }
                
                if (sum < target) {
                    left++;
                } else if (sum > target) {
                    right--;
                } else {
                    return target; // The sum is equal to the target, so it's the closest.
                }
            }
        }
        
        return closest_sum;
    }
};
