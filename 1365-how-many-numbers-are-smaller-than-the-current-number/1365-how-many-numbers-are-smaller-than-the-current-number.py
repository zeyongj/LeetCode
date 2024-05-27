class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            c = 0
            for j in nums:
                if i > j:
                    c += 1
            l.append(c)
        return l