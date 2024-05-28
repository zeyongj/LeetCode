class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Sliding Window
        size = len(s)
        
        if size == 0:
            return 0
        
        max_len = 0
        start = 0
        
        cost = 0
        
        for i in range(size):
            cost += abs(ord(s[i]) - ord(t[i])) # Covert char to ascii
            
            # Remove the indices from the left end till the cost becomes less than the allowed
            while cost > maxCost:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            max_len = max(max_len, i - start + 1)
        
        return max_len