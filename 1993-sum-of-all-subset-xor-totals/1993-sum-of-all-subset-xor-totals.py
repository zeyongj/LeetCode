class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0  # Total sum of XORs of all subsets

        def dfs(index: int, current_xor: int):
            if index == len(nums):
                self.total += current_xor
                return
            # Include current number
            dfs(index + 1, current_xor ^ nums[index])
            # Exclude current number
            dfs(index + 1, current_xor)

        dfs(0, 0)
        return self.total