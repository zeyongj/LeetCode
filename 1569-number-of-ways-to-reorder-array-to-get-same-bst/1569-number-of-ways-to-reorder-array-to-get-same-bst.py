class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        M = 1_000_000_007

        def num_ways(bst: Sequence[int]) -> int:
            if len(bst) <= 2: return 1
            lefts, rights = [x for x in bst if x < bst[0]], [x for x in bst if x > bst[0]]
            return num_ways(lefts) * num_ways(rights) * comb(len(lefts) + len(rights), len(lefts)) % M
        
        return (num_ways(nums) - 1) % M
