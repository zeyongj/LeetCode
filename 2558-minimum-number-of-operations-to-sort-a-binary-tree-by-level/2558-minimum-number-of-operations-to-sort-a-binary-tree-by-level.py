# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swap(arr: List[int]) -> int:
            pos = {m:j for j,m in enumerate(sorted(arr))}  
            visited = [0 for _ in range(len(arr))]
            num_swap = 0
            for i in range(n):
                cnt = 0
                while not visited[i] and i != pos[arr[i]]:
                    visited[i], i = 1, pos[arr[i]]
                    cnt += 1
                num_swap += max(0, cnt - 1)
            return num_swap

        dq, res = collections.deque([root]), 0
        while dq:
            vals = []
            n = len(dq)
            for _ in range(n):
                node = dq.popleft()
                vals.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            res += min_swap(vals)
        return res