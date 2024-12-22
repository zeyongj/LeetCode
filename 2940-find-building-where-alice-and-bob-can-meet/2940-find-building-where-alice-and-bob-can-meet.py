class SegNode():
    def __init__(self,val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # segment tree implementation, 
        def construct_segment_tree(l, r):

            nonlocal heights
            if l == r:
                return SegNode(((l,r),heights[l]), None, None)
            
            else:
                mid = (l + r) // 2
                left, right = construct_segment_tree(l, mid), construct_segment_tree(mid + 1, r)
                return SegNode(((l,r),max(left.val[1], right.val[1])), left, right)

        # wanna see the constructed seg tree, refer the commented out code below, 

        """
        tr = construct_segment_tree(0, len(heights) - 1)
        def recur(root):
            if not root:
                return 
            print(root.val)
            recur(root.right)
            recur(root.left)
        recur(tr)
        """

        def overlap(a,b,l,r):

            """

            1 -- partial-overlap
            2 -- complete-overlap
            3 -- no-overlap

            """
            if a <= l and b >= r:
                return 2
            elif r < a or b < l:
                return 3
            else:
                return 1
        
        root = construct_segment_tree(0, len(heights) - 1)
        max_between_intervals_cache = {}

        def max_between_intervals(a,b,root):
            # search on the segment tree with cache
        
            l, r = root.val[0]
            overlap_status = overlap(a,b,l,r)

            if overlap_status == 2:
                return root.val[1]
            elif overlap_status == 3:
                return -inf
            else:
                return max(max_between_intervals(a,b,root.left), max_between_intervals(a,b,root.right))


        def binary_search(i, req):
            nonlocal root
            l, r = i, len(heights) - 1

            while l < r:
                mid = (l + r) // 2
                if (l,mid) in max_between_intervals_cache:
                    mx_b_interval = max_between_intervals_cache[(l,mid)]
                else:
                    mx_b_interval = max_between_intervals(l,mid, root)
                    max_between_intervals_cache[(l,mid)] = mx_b_interval

                if mx_b_interval > req:
                    r = mid
                else:
                    l = mid + 1
            
            return r if heights[r] > req else -1
        
        answer = []
        root = construct_segment_tree(0, len(heights) - 1)

        for l, r in queries:
            l, r = min(l,r), max(l,r)
            if heights[l] < heights[r] or l == r:
                answer.append(r)
            
            else:
                answer.append(binary_search(r + 1, heights[l]))
            
        
        return answer