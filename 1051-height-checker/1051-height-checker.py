class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h !=s for h, s in zip(heights, sorted(heights)))