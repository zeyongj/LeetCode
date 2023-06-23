#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int index = 0;
        
        // add all intervals that end before newInterval starts
        while(index < intervals.size() && intervals[index][1] < newInterval[0]){
            result.push_back(intervals[index++]);
        }

        // merge all overlapping intervals
        while(index < intervals.size() && intervals[index][0] <= newInterval[1]){
            newInterval[0] = min(newInterval[0], intervals[index][0]);
            newInterval[1] = max(newInterval[1], intervals[index][1]);
            index++;
        }

        // add the merged interval
        result.push_back(newInterval);

        // add remaining intervals
        while(index < intervals.size()){
            result.push_back(intervals[index++]);
        }

        return result;
    }
};
