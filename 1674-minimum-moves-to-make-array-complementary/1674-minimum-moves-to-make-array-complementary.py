class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            vala, valb = sorted([nums[i], nums[n - 1 - i]])
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            diff[vala + 1] -= 1
            diff[valb + limit + 1] += 1
            diff[vala + valb] -= 1
            diff[vala + valb + 1] += 1
        res, cur = n, 0
        for i in range(2, 2 * limit + 1):
            cur += diff[i]
            res = min(res, cur)
        return res