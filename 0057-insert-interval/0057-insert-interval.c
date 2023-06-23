class Solution:
    def insert(self, intervals, newInterval):
        result = []
        index = 0

        # add all intervals that end before newInterval starts
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1

        # merge all overlapping intervals
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1

        # add the merged interval
        result.append(newInterval)

        # add remaining intervals
        while index < len(intervals):
            result.append(intervals[index])
            index += 1

        return result
