class SegmentTree:
    """Segment Tree over array of size n"""

    def __init__(self, n: int):
        self.n = n
        self.size = 4 * n
        self.sum = [0] * self.size
        self.min = [0] * self.size
        self.max = [0] * self.size

    def _pull(self, node: int):
        """Helper to recompute information of node by it's children"""

        l, r = node * 2, node * 2 + 1

        self.sum[node] = self.sum[l] + self.sum[r]
        self.min[node] = min(self.min[l], self.sum[l] + self.min[r])
        self.max[node] = max(self.max[l], self.sum[l] + self.max[r])

    def update(self, idx: int, val: int):
        """Update value by index idx in original array"""

        node, l, r = 1, 0, self.n - 1
        path = []

        while l != r:
            path.append(node)
            m = l + (r - l) // 2
            if idx <= m:
                node = node * 2
                r = m
            else:
                node = node * 2 + 1
                l = m + 1

        self.sum[node] = val
        self.min[node] = val
        self.max[node] = val

        while path:
            self._pull(path.pop())

    def find_rightmost_prefix(self, target: int = 0) -> int:
        """Find rightmost index r with prefixsum(r) = target
        prefixsum(i) = sum(arr[j] for j in range(i + 1))"""

        node, l, r, sum_before = 1, 0, self.n - 1, 0

        def _exist(node: int, sum_before: int):
            return self.min[node] <= target - sum_before <= self.max[node]

        if not _exist(node, sum_before):
            return -1

        while l != r:
            m = l + (r - l) // 2
            lchild, rchild = node * 2, node * 2 + 1

            # Check right half first
            sum_before_right = self.sum[lchild] + sum_before
            if _exist(rchild, sum_before_right):
                node = rchild
                l = m + 1
                sum_before = sum_before_right
            else:
                node = lchild
                r = m

        return l


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        stree = SegmentTree(n)  # SegmentTree over balance array for current l
        first = dict()  # val -> first occurence idx for current l

        result = 0
        for l in reversed(range(n)):
            num = nums[l]
    
            # If x already had a first occurrence to the right, remove that old marker.
            if num in first:
                stree.update(first[num], 0)

            # Now x becomes first occurrence at l.
            first[num] = l
            stree.update(l, 1 if num % 2 == 0 else -1)

            # Find rightmost r >= l such that sum(w[l..r]) == 0
            r = stree.find_rightmost_prefix(target=0)
            if r >= l:
                result = max(result, r - l + 1)

        return result