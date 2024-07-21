class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int min = INT_MAX;
        for(int i = 0; i < points.size(); i++) {
            if( (x == points[i][0]) || (y == points[i][1]) ) {
                int d = abs(points[i][0] - x) + abs(points[i][1] - y);
                if(d < min) min = d; 
            }
        }

        for(int i = 0; i < points.size(); i++) {
            if( (x == points[i][0]) || (y == points[i][1]) ) {
                int d1 = abs(points[i][0] - x) + abs(points[i][1] - y); 
                if(d1 == min) return i;
            }
        }
        return -1;
    }
};