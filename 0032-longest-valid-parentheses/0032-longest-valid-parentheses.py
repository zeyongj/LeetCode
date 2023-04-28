class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0
        st = [-1] # Base for calculating the length
        
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i) # Update the base for length calculation
                else:
                    maxLength = max(maxLength, i - st[-1])
        
        return maxLength
