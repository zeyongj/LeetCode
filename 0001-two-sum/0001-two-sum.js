public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        if(nums == null || nums.Length < 2)
            return new int[2];
        
        Dictionary<int,int> dic = new Dictionary<int,int>();
        
        for(int i = 0; i < nums.Length; i++)
        {
            if(dic.ContainsKey(target - nums[i]))
                return new int[]{i, dic[target - nums[i]]};
            else if(!dic.ContainsKey(nums[i]))
                dic.Add(nums[i], i);
        }
        
        return new int[2];
    }
}