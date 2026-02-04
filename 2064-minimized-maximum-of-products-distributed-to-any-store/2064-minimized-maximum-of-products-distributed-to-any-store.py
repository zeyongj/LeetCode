class Solution:
    def solve(self, n, quantities, item):
        if item == 0:
            return False
        store = 0
        for product in quantities:
            store += (product - 1) // item + 1
            if store > n:
                return False
        return True

    def minimizedMaximum(self, n, quantities):
        low = 1
        high = max(quantities)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if self.solve(n, quantities, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans