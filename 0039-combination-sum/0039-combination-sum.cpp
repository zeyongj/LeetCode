#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current_combination;
        
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, 0, current_combination, result);
        
        return result;
    }
    
    void dfs(vector<int>& candidates, int target, int start, vector<int>& current_combination, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(current_combination);
            return;
        }
        
        for (int i = start; i < candidates.size() && candidates[i] <= target; ++i) {
            current_combination.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i, current_combination, result);
            current_combination.pop_back();
        }
    }
};
