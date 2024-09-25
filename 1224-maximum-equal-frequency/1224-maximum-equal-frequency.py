class Solution:
    def maxEqualFreq(self, nums):
        counts, freq = collections.Counter(), collections.Counter()
        res = 0
        for i, num in enumerate(nums):
            # update counts
            counts[num] += 1
            # update counts with that frequency
            freq[counts[num]] += 1

            count = freq[counts[num]] * counts[num]
            if count == i + 1 and i != len(nums) - 1: # case 1
                res = max(res, i + 2)
            elif count == i: # case 2
                res = max(res, i + 1)
        return res