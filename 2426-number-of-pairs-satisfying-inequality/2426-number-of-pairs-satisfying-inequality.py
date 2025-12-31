class Bit:

    def __init__(self, n: int):
        self.bit = [0 for _ in range(n + 1)]

    def update(self, i: int, val: int) -> None:
        i += 1
        while i < len(self.bit):
            self.bit[i] += val
            i += self._find_RSB(i)

    def prefix_sum(self, i: int) -> int:
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= self._find_RSB(i)
        return s 

    def _find_RSB(self, i: int) -> int:
        return i & -i


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        res, shift = 0, 2 * 10 ** 4
        bit = Bit(10 ** 5)
        for i in range(len(nums1)):
            d = nums1[i] - nums2[i]
            res += bit.prefix_sum(d + diff + shift)
            bit.update(d + shift, 1)
        return res