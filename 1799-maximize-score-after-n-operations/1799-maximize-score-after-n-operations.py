class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def backtrack(mask):
            w = mask.bit_count() // 2
            if 2 * w == len(nums):
                return 0
            max_score = 0
            for i in range(len(nums) - 1):
                if (mask >> i) & 1 == 1:
                    continue
                for j in range(i + 1, len(nums)):
                    if (mask >> j) & 1 == 1:
                        continue
                    score1 = math.gcd(nums[i], nums[j]) * (w + 1)
                    new_mask = mask | (1 << i) | (1 << j)
                    score2 = backtrack(new_mask)
                    max_score = max(max_score, score1 + score2)
            return max_score
        return backtrack(0)