class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dict = {}
        for x in nums:
            dict[x] = dict.get(x, 0) + 1
        for k, v in dict.items():
            if (v & 1):
                return False
        return True