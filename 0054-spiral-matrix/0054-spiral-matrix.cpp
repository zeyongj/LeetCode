#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int m = matrix.size();
        int n = matrix[0].size();
        
        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;
        
        while(true) {
            // Traverse from left to right.
            for (int i = left; i <= right; i++) res.push_back(matrix[top][i]);
            if (++top > bottom) break;

            // Traverse from top to bottom.
            for (int i = top; i <= bottom; i++) res.push_back(matrix[i][right]);
            if (--right < left) break;

            // Traverse from right to left.
            for (int i = right; i >= left; i--) res.push_back(matrix[bottom][i]);
            if (--bottom < top) break;

            // Traverse from bottom to top.
            for (int i = bottom; i >= top; i--) res.push_back(matrix[i][left]);
            if (++left > right) break;
        }
        
        return res;
    }
};
