class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}
        def helper(screen, clipboard):
            if (screen, clipboard) in cache: 
                return cache[(screen, clipboard)]
            if screen == n: 
                return 0
            if screen > n: 
                return float("Inf")
            
            copy_paste = helper(screen+screen, screen) + 2
            paste = float("Inf")
            if clipboard:
                paste = helper(screen + clipboard, clipboard) + 1

            cache[(screen, clipboard)] = min(copy_paste, paste)    
            return cache[(screen, clipboard)]
        
        return helper(1, 0)