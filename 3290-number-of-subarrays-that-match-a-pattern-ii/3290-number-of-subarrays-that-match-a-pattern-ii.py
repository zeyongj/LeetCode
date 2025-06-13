class Solution:
    def countMatchingSubarrays(self, nums: List[int], pat: List[int]) -> int:
        # Based on the given condition, compute the txt.
        txt = []
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                txt.append(1)
            elif nums[i+1] == nums[i]:
                txt.append(0)
            else:
                txt.append(-1)
        
        def KMP(pat, txt):
            res = 0
            n, m = len(txt), len(pat)
            
            # Preprocess the pattern (calculate lps[] array)
            lps = computeLPS(pat)
            
            i = 0 # index for txt[]
            j = 0 # index for pat[]
            while i < n:
                if txt[i] == pat[j]:
                    i += 1
                    j += 1
                    
                if j == m:
                    res += 1
                    j = lps[j-1]
                elif i < n and txt[i] != pat[j]:
                    if j != 0:
                        j = lps[j-1]
                    else:
                        i += 1
            return res
        
        def computeLPS(pat):
            """
                create lps[] that will hold the longest prefix suffix
                values for pattern
            """
            lps = [0] * len(pat) # lps[0] is always 0
            l = 0  # length of the previous longest prefix suffix
            i = 1
            while i < len(pat):
                
                if pat[i] == pat[l]:
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if l != 0:
                        l = lps[l-1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        return KMP(pat, txt)