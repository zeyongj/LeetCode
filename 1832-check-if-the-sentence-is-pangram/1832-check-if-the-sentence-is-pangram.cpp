class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> seen(sentence.begin(), sentence.end());
        
        if (seen.size() == 26)
            return true;
        else
            return false;
    }
};