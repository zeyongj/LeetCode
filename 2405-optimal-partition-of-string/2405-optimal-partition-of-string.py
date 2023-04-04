class Solution(object):
    def partitionString(self, s):
        idx = 0
        count = 0
        mp = {}
        while idx < len(s):
            if s[idx] in mp: 
                count += 1
                mp.clear()
            mp[s[idx]] = True
            idx += 1
        return count + 1