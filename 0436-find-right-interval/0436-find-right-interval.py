class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        res = [-1] * n
        for i in range(n):
            intervals[i].append(i)

        def binary_search(ele):
            left, right = 0, n-1
            ans = float('inf')
            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][0] >= ele:
                    ans = min(ans, mid)
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
                
        intervals.sort()
        for i in intervals:
            val = binary_search(i[1])
            if val != float('inf'):
                res[i[2]] = intervals[val][2]

        return res