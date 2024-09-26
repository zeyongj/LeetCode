class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        st = set()
        leftmost = [1e5]*26
        rightmost = [0] * 26

        for i in range(len(s)):
            leftmost[ord(s[i]) - ord('a')] = min(leftmost[ord(s[i]) - ord('a')], i)
            rightmost[ord(s[i]) - ord('a')] = i

        res = 0

        for i in range(26):
            if leftmost[i] < rightmost[i]:
                first_occurrence = leftmost[i]
                last_occurrence = rightmost[i]
                for j in range(first_occurrence + 1, last_occurrence):
                    st.add(s[j])
                res += len(st)
                st.clear()

        return res
