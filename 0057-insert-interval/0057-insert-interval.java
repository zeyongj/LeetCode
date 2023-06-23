import java.util.*;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int index = 0;

        // add all intervals that end before newInterval starts
        while (index < intervals.length && intervals[index][1] < newInterval[0]) {
            result.add(intervals[index++]);
        }

        // merge all overlapping intervals
        while (index < intervals.length && intervals[index][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[index][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[index][1]);
            index++;
        }

        // add the merged interval
        result.add(newInterval);

        // add remaining intervals
        while (index < intervals.length) {
            result.add(intervals[index++]);
        }

        // convert List to array
        return result.toArray(new int[result.size()][]);
    }
}
