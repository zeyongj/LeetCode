class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_set = set()
        for i in nums :
            if i not in new_set :
                new_set.add(i)
            else :
                return i
        return nums[0]