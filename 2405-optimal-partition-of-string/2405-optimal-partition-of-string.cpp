#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int partitionString(string s) {
        int idx = 0;
        int count = 0;
        unordered_map<char, bool> mp; 
        while (idx < s.length()) {
            if (mp.find(s[idx]) != mp.end()) { 
                count++; 
                mp.clear(); 
            }
            mp[s[idx]] = true; 
            idx++; 
        }
        return ++count;
    }
};
