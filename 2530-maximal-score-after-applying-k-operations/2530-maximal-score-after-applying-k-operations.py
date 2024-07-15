class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        res = 0
        heap = heapq.heapify(nums)
        for _ in range(k):
            a = heapq.heappop(nums) * -1
            res += a
            heapq.heappush(nums, -math.ceil(a/3))
        return res