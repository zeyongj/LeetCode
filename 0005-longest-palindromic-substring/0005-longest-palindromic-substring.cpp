class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        if (n <= 1) return s;
        int start = 0, len = 1;
        for (int i = 0; i < n; ) {
            int j = i, k = i;
            while (k < n - 1 && s[k + 1] == s[k]) ++k; // skip duplicate characters
            i = k + 1;
            while (j > 0 && k < n - 1 && s[j - 1] == s[k + 1]) { // expand from center
                --j;
                ++k;
            }
            int newLen = k - j + 1;
            if (newLen > len) {
                start = j;
                len = newLen;
            }
        }
        return s.substr(start, len);
    }
};
