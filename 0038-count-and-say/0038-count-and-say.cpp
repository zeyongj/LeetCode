#include <string>

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        
        string previous = countAndSay(n - 1);
        string result = "";
        int count = 1;
        
        for (int i = 1; i < previous.length(); ++i) {
            if (previous[i] == previous[i - 1]) {
                count++;
            } else {
                result += to_string(count) + previous[i - 1];
                count = 1;
            }
        }
        
        result += to_string(count) + previous[previous.length() - 1];
        
        return result;
    }
};
