public class Solution {
    public int LongestValidParentheses(string s) {
        int maxLength = 0;
        int length = s.Length;
        int[] stack = new int[length + 1];
        int top = 0;
        stack[top] = -1; // Base for calculating the length

        for (int i = 0; i < length; i++) {
            if (s[i] == '(') {
                stack[++top] = i;
            } else {
                top--;
                if (top == -1) {
                    stack[++top] = i; // Update the base for length calculation
                } else {
                    maxLength = Math.Max(maxLength, i - stack[top]);
                }
            }
        }
        return maxLength;
    }
}