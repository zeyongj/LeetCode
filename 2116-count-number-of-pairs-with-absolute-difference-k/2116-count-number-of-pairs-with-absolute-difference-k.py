class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            counter += seen[num-k] + seen[num+k]
            seen[num] += 1
        return counter