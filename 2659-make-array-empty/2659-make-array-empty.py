from sortedcontainers import SortedList
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList((num, i) for i, num in enumerate(nums))
        sl_idx = SortedList(range(n))
        start, ans = 0, 0
        while sl:
            num, i = sl.pop(0)
            ans += self.count(sl_idx, n, start, i)
            sl_idx.remove(i)
            start = (i + 1) % n
        return ans
    
    def count(self, sl, n, start, end):
        if start <= end:
            return sl.bisect(end) - sl.bisect_left(start)
        else:
            return self.count(sl, n, start, n - 1) + self.count(sl, n, 0, end)