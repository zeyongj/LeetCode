public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new List<int[]>();
        int i = 0;
        
        for (;i < intervals.Length && intervals[i][1] < newInterval[0]; i++)
            res.Add(intervals[i]);
        
        for (;i < intervals.Length && newInterval[0] <= intervals[i][1] && newInterval[1] >= intervals[i][0]; i++)
            newInterval = new int[] { Math.Min(intervals[i][0], newInterval[0]), Math.Max(intervals[i][1], newInterval[1]) };
        
        res.Add(newInterval);
        
        for (;i < intervals.Length; i++)
                res.Add(intervals[i]);
        
        return res.ToArray();
    }
}