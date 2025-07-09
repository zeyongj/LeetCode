class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while "abc" in s:
            s = s.replace("abc", "")
        return not s