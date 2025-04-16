class Solution(object):
    def countGood(self, nums, k):
        mpp = {}
        cnt = left = 0
        for i in range(len(nums)):
            if nums[i] not in mpp:
                mpp[nums[i]] = 0
            k -= mpp[nums[i]]
            mpp[nums[i]] += 1
            while k <= 0:
                mpp[nums[left]] -= 1
                k += mpp[nums[left]]
                left += 1
            cnt += left
        return cnt