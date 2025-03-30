class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        L = len(s)
        last = {s[i]: i for i in range(L)} # last appearance of the letter
        i, ans = 0, []
        while i < L:
            end, j = last[s[i]], i + 1
            while j < end: # validation of the part [i, end]
                if last[s[j]] > end:
                    end = last[s[j]] # extend the part
                j += 1
           
            ans.append(end - i + 1)
            i = end + 1
            
        return ans