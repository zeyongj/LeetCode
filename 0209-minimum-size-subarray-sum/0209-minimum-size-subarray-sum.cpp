#include<vector>
#include<climits>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, right = 0;
        int sum = 0;
        int min_len = INT_MAX;
        
        while(right < nums.size()){
            sum += nums[right];
            
            while(sum >= target){
                min_len = min(min_len, right - left + 1);
                sum -= nums[left];
                left++;
            }
            right++;
        }
        return (min_len != INT_MAX) ? min_len : 0;
    }
};
