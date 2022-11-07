class Solution {
public:
    int maximum69Number (int num) {
        string numString = to_string(num);
        for (auto &currChar : numString) {
            if (currChar == '6') {
                currChar = '9';
                break;
            }
        }
        return stoi(numString);
    }
};