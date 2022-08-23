class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        unordered_map<char, char> mp = { {')', '('}, {']', '['}, {'}', '{'} };
        for (int i = 0; i < s.size(); i ++){
            if (s[i] == '(' || s[i] == '[' || s[i] == '{')
                st.push(s[i]);
            else{
                if (st.size() && mp[s[i]] == st.top()) st.pop();
                else return false;
            }
        }
        return st.empty();
    }
};