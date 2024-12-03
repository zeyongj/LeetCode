class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m, n=len(spaces), len(s)
        t=[' ']*(m+n)
        j=0
        for i, c in enumerate(s):
            if j<m and i==spaces[j]:
                j+=1
            t[i+j]=s[i]
        return "".join(t)       