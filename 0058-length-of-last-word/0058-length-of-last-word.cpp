#include<string>

class Solution {
public:
    int lengthOfLastWord(std::string s) {
        int length = 0;
        int pos = s.length() - 1;

        // Skip trailing spaces if any
        while (pos >= 0 && s[pos] == ' ') {
            --pos;
        }

        // Count characters in the last word
        while (pos >= 0 && s[pos] != ' ') {
            --pos;
            ++length;
        }

        return length;
    }
};
