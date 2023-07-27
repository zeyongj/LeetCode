#include<vector>
#include<string>
using namespace std;

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int i = 0, n = words.size();
        while (i < n) {
            int totalChars = words[i].size();
            int j = i + 1;
            while (j < n && totalChars + 1 + words[j].size() <= maxWidth) {
                totalChars += 1 + words[j].size();
                ++j;
            }
            int spaceSlots = j - i - 1;
            int totalSpaces = maxWidth - totalChars + spaceSlots;

            string line = words[i];
            for(int k = i + 1; k < j; ++k){
                int spaces = j == n || spaceSlots == 0 ? 1 : totalSpaces/spaceSlots + (k - i <= totalSpaces%spaceSlots);
                line += string(spaces, ' ') + words[k];
            }
            line += string(maxWidth - line.size(), ' ');
            res.push_back(line);
            i = j;
        }
        return res;
    }
};
