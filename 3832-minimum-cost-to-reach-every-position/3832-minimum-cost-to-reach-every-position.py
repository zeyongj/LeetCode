class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = [0] * len(cost)
        for i in range(len(cost)):
            ans[i] = min(ans[i - 1] if i > 0 else float('inf'), cost[i])
        return ans