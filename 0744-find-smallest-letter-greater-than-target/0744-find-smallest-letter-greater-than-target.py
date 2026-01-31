class Solution:
    def nextGreatestLetter(self, L: List[str], target: str) -> str:
        return L[i] if (i:=bisect_right(L, target))<len(L) else L[0]
        