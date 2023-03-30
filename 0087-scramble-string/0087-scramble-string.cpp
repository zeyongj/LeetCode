#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    unordered_map<string, bool> memo;

    bool isScramble(string s1, string s2) {
        if (s1.length() != s2.length()) return false;
        if (s1 == s2) return true;
        if (memo.count(s1 + "_" + s2)) return memo[s1 + "_" + s2];

        string sorted_s1 = s1;
        string sorted_s2 = s2;
        sort(sorted_s1.begin(), sorted_s1.end());
        sort(sorted_s2.begin(), sorted_s2.end());
        if (sorted_s1 != sorted_s2) return false;

        int n = s1.length();
        for (int i = 1; i < n; ++i) {
            if ((isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i))) ||
                (isScramble(s1.substr(0, i), s2.substr(n - i)) && isScramble(s1.substr(i), s2.substr(0, n - i)))) {
                return memo[s1 + "_" + s2] = true;
            }
        }

        return memo[s1 + "_" + s2] = false;
    }
};
