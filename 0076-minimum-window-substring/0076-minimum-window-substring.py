class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict

        if not s or not t:
            return ""
        
        # Dictionary to keep the count of all unique characters in t
        dict_t = Counter(t)
        
        # Number of unique characters in t that must be present in the window
        required = len(dict_t)
        
        # Left and right pointer
        l, r = 0, 0
        
        # Formed is used to keep track of how many unique characters in t are currently present in the window in desired frequency
        formed = 0
        
        # Dictionary to keep the count of all characters in the current window
        window_counts = defaultdict(int)
        
        # Tuple (window length, left, right)
        ans = float("inf"), None, None
        
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] += 1
            
            # If the frequency of the current character added equals to the desired count in t, increment the formed count
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try and contract the window till the point where it ceases to be 'desirable'
            while l <= r and formed == required:
                character = s[l]
                
                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                # Move the left pointer ahead
                l += 1
            
            # Keep expanding the window by moving the right pointer
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
