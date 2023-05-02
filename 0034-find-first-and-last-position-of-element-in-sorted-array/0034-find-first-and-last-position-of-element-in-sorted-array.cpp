#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = findStartingIndex(nums, target);
        int end = findEndingIndex(nums, target);
        return {start, end};
    }

private:
    int findStartingIndex(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid;

        while (left <= right) {
            mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                if (mid == 0 || nums[mid - 1] < target) {
                    return mid;
                }
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    int findEndingIndex(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid;

        while (left <= right) {
            mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                if (mid == nums.size() - 1 || nums[mid + 1] > target) {
                    return mid;
                }
                left = mid + 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
};
