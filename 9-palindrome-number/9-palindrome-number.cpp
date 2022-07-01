class Solution {
    public: 
    bool isPalindrome(int x) {
        string s = to_string(x);    
        return s == string(rbegin(s), rend(s));
    }
};