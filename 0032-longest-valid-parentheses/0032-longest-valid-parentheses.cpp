#include <iostream>
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int maxLength = 0;
        stack<int> st;
        st.push(-1); // Base for calculating the length

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                st.push(i);
            } else {
                st.pop();
                if (st.empty()) {
                    st.push(i); // Update the base for length calculation
                } else {
                    maxLength = max(maxLength, i - st.top());
                }
            }
        }
        return maxLength;
    }
};
