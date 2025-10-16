class Solution(object):
    def findSmallestInteger(self, nums, value):
        rem = [0] * value
        for x in nums:
            r = (x % value + value) % value
            rem[r] += 1
        res = 0
        while rem[res % value]:
            rem[res % value] -= 1
            res += 1
        return res