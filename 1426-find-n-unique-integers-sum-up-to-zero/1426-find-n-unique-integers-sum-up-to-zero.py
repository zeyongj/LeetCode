class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-(n>>1), 0))+list(range((n&1)==0, (n>>1)+1))