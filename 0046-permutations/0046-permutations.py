from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            # If all integers are used up
            if start == end:
                output.append(nums[:])
            for i in range(start, end):
                # place i-th integer first
                # then use next integers to complete the permutations
                nums[start], nums[i] = nums[i], nums[start]
                # use next integers to complete the permutations
                backtrack(start + 1, end)
                # backtrack
                nums[start], nums[i] = nums[i], nums[start]

        output = []
        n = len(nums)
        backtrack(0, n)
        return output
