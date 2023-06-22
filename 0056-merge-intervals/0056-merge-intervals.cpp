#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> merged{{intervals[0]}};
        
        for (int i = 1; i < intervals.size(); ++i) {
            // If the current interval does not overlap with the last merged interval,
            // append it to the merged intervals.
            if (merged.back()[1] < intervals[i][0]) {
                merged.push_back(intervals[i]);
            }
            // Otherwise, there is overlap, so we merge the current and last interval.
            else {
                merged.back()[1] = max(merged.back()[1], intervals[i][1]);
            }
        }
        return merged;
    }
};
