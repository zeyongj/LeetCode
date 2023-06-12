public class Solution {
    public IList<string> SummaryRanges(int[] nums) {
        if (nums == null || nums.Length == 0)
            return new List<string>();
        
        List<string> res = new List<string>();
        int i = 0;
        
        for (int j = 0; j < nums.Length - 1; j++)
            if (nums[j] + 1 != nums[j + 1])
            {
                res.Add(nums[i] == nums[j] ? nums[i].ToString() : nums[i].ToString() + "->" + nums[j].ToString());
                i = j + 1;
            }
        
        res.Add(i == nums.Length - 1 ? nums[i].ToString() : nums[i].ToString() + "->" + nums[nums.Length - 1].ToString());
        
        return res;
    }
}