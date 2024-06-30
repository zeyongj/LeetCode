class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            ans = 2 * min(x,y)
        else: ans = 2 * min(x,y) + 1 
            
        ans += z

        return ans * 2 