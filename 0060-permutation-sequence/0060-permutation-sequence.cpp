#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> factorial(n, 1);
        vector<char> num(n, 1);
        string res;
        
        // Precompute factorials
        for (int i = 1; i < n; i++) {
            factorial[i] = factorial[i-1] * i;
        }
        // Create a list of numbers
        for (int i = 0; i < n; i++) {
            num[i] = '1' + i;
        }
        
        k--;
        for (int i = n; i >= 1; i--) {
            int j = k / factorial[i-1];
            k %= factorial[i-1];
            res.push_back(num[j]);
            num.erase(num.begin() + j);
        }
        return res;
    }
};
