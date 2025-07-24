class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        return [(n & 0b10101010101).bit_count(), (n & 0b01010101010).bit_count()]