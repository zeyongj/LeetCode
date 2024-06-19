class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        Min = 101
        ans = []
        size = len(s)
        for i in range(size):
            for j in range(i, size + 1):
                if s[i:j].count('1') == k:
                    ans.append(s[i:j])
                    if Min > len(s[i:j]): 
                        Min = len(s[i:j])
                        
        ans.sort()
        for i in ans:
            if len(i) == Min: 
                return i
        return ''