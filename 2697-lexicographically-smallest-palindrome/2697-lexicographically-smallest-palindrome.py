class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1

        s = list(s)
        while i <j:

            if s[i]!=s[j]:
                if s[i]<s[j]:
                    s[j] = s[i]
                elif s[i]>s[j]:
                    s[i] = s[j]
            i+=1
            j-=1

        return ''.join(s)