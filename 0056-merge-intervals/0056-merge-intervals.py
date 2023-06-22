class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for i in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, append it
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], i[1])

        return merged
