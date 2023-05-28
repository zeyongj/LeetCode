public class Solution {
    public IList<IList<int>> PermuteUnique(int[] nums) {
        var results = new List<IList<int>>();
        Array.Sort(nums);  // It is important to sort the array, so duplicates are grouped together
        PermuteUnique(nums, new bool[nums.Length], new List<int>(), results);
        return results;
    }
    
    private void PermuteUnique(int[] nums, bool[] used, List<int> path, IList<IList<int>> results) {
        if (path.Count == nums.Length) {
            results.Add(new List<int>(path));
            return;
        }
        
        for (int i = 0; i < nums.Length; i++) {
            if (used[i]) continue;  // Skip if the number is already used
            
            // If the current number is the same as the previous one and the previous one is not used, skip
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            
            used[i] = true;
            path.Add(nums[i]);
            PermuteUnique(nums, used, path, results);
            path.RemoveAt(path.Count - 1);  // Backtrack
            used[i] = false;
        }
    }
}
