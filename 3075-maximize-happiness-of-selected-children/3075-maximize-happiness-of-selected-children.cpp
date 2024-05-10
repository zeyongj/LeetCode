#include <vector>
#include <algorithm>  // For sort and max
using namespace std;

class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        // Sorting in descending order
        sort(happiness.begin(), happiness.end(), greater<int>());

        int i = 0;
        long long res = 0;

        while (k > 0 && i < happiness.size()) {
            happiness[i] = max(happiness[i] - i, 0);
            res += happiness[i];
            i++;
            k--;
        }

        return res;        
    }
};