#include<vector>
#include<algorithm> // to use max function

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int altitude = 0;
        int maxAltitude = 0;
        
        for (int i = 0; i < gain.size(); i++) {
            altitude += gain[i];
            maxAltitude = max(maxAltitude, altitude);
        }
        
        return maxAltitude;
    }
};
