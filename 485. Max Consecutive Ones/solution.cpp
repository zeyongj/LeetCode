# include<algorithm>
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int result = 0;
        // int ans = 0;
        if (nums.empty())
            return 0;
        else {
            count = 0;
            result = 0;
            for (int i = 0; i < nums.size(); i++) { // Traversal
                if (nums [i] == 1)
                    count ++;
                else {
                    result = max(result, count);
                    count = 0;
                }
            }
            // ans = max(result, count);
            return max(result, count);
        }
    }
};
