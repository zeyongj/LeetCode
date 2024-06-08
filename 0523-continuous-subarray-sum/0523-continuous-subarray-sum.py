class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        mod_seen = {0: -1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                # ensures that the size of subarray is at least 2
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                # mark the value of prefix_mod with the current index.
                mod_seen[prefix_mod] = i

        return False