class Solution:
    def minimumChairs(self, s: str) -> int:
        stack = []
        ans = 0
        
        for i in s:
            if i == "E":
                stack.append(i)
                length = len(stack)
                if length > ans:
                    ans = length
            if i == "L":
                stack.pop()
        
        return ans