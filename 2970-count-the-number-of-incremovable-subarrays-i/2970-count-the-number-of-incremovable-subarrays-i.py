class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                ok = True
                lst = -1

                for k in range(n):
                    if i <= k <= j:
                        continue
                    else:
                        ok &= lst < nums[k]
                        lst = nums[k]

                ans += int(ok)
        return ans
