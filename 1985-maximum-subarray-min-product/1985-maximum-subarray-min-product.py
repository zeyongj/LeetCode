class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left_bound, right_bound = [0] * n, [0] * n
        st = []
        for i in range(0, n):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            if len(st) > 0:
                left_bound[i] = st[-1] + 1
            else:
                left_bound[i] = 0
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            if len(st) > 0:
                right_bound[i] = st[-1] - 1
            else:
                right_bound[i] = n - 1
            st.append(i)

        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        def getSum(left, right):  # left, right inclusive
            return preSum[right + 1] - preSum[left]

        maxProduct = 0
        for i in range(n):
            maxProduct = max(maxProduct, nums[i] * getSum(left_bound[i], right_bound[i]))
        return maxProduct % 1000_000_007