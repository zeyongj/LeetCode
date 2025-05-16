class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        new_set = set()
        for i in nums :
            if i not in new_set :
                new_set.add(i)
            else :
                return i
        return nums[0]        