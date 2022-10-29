#include <string>
class Solution {
    std::string source, target;
    int leftBound, rightBound;

    private: bool rec_isSubsequence(int leftIndex, int rightIndex) {
        if (leftIndex == leftBound)
            return true;
        if (rightIndex == rightBound)
            return false;

        if (source.at(leftIndex) == target.at(rightIndex))
            leftIndex++;
        rightIndex++;

        return rec_isSubsequence(leftIndex, rightIndex);
    }

    public: bool isSubsequence(std::string s, std::string t) {
        this->source = s;
        this->target = t;
        this->leftBound = s.length();
        this->rightBound = t.length();

        return rec_isSubsequence(0, 0);
    }
};