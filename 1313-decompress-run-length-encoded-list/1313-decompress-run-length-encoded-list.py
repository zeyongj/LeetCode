class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return reduce(
            lambda x, y: x + y,
            (f * [v] for f, v in list(zip(*([iter(nums)] * 2)))),
        )