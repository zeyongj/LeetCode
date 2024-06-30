class Solution(object):
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        if x == y:
            ans = 2 * min(x,y)
        else: ans = 2 * min(x,y) + 1 
            
        ans += z

        return ans * 2         