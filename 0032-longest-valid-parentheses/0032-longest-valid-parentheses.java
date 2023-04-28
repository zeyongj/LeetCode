import java.util.Stack;

class Solution {
    public int longestValidParentheses(String s) {
        int maxLength = 0;
        Stack<Integer> st = new Stack<>();
        st.push(-1); // Base for calculating the length

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                st.push(i);
            } else {
                st.pop();
                if (st.empty()) {
                    st.push(i); // Update the base for length calculation
                } else {
                    maxLength = Math.max(maxLength, i - st.peek());
                }
            }
        }
        return maxLength;
    }
}