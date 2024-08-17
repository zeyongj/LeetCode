class Solution:
    def minFlips(self, s: str) -> int:
        s = s + s
        size = len(s)
        alt_string_1 = "01"*(size//2)
        alt_string_2 = "10"*(size//2)
        
        res = size
        left = 0
        diff_count_1 = 0
        diff_count_2 = 0

        for right, char in enumerate(s):
            if char != alt_string_1[right]:
                diff_count_1 += 1
            if char != alt_string_2[right]:
                diff_count_2 += 1
            
            # if window is original size of s
            if (right-left+1) == size/2:
                res = min(diff_count_1, diff_count_2, res)

                if s[left] != alt_string_1[left]:
                    diff_count_1 -= 1
                if s[left] != alt_string_2[left]:
                    diff_count_2 -= 1
                
                left += 1
        
        return res