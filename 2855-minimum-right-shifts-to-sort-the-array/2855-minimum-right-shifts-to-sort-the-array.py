class Solution(object):
    def minimumRightShifts(self, nums):
        drop = 999

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if drop < 999:
                    return -1
                drop = i

        if drop == 999:
            return 0

        if nums[-1] > nums[0]:
            if drop < 999:
                return -1
            drop = i

        return len(nums) - drop - 1