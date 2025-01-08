class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        m, curr_day = {}, 0
        for x in tasks:
            curr_day += 1
            if x in m and curr_day - m[x] <= space:
                curr_day += space - (curr_day - m[x]) + 1
            m[x] = curr_day
        return curr_day 