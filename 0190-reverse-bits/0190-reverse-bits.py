class Solution:
    def reverseBits(self, n: int) -> int:
        k='{0:032b}'.format(n)
        j=k[::-1]
        return int(j,2)