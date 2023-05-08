public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        List<IList<int>> result = new List<IList<int>>();
        List<int> currentCombination = new List<int>();
        Array.Sort(candidates);
        dfs(candidates, target, 0, currentCombination, result);
        return result;
    }
    
    private void dfs(int[] candidates, int target, int start, List<int> currentCombination, List<IList<int>> result) {
        if(target == 0) {
            result.Add(new List<int>(currentCombination));
            return;
        }
        
        for(int i = start; i < candidates.Length && candidates[i] <= target; i++) {
            currentCombination.Add(candidates[i]);
            dfs(candidates, target - candidates[i], i, currentCombination, result);
            currentCombination.RemoveAt(currentCombination.Count - 1);
        }
    }
}
