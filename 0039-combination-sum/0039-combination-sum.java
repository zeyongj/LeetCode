import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentCombination = new ArrayList<>();
        
        Arrays.sort(candidates);
        dfs(candidates, target, 0, currentCombination, result);
        
        return result;
    }
    
    private void dfs(int[] candidates, int target, int start, List<Integer> currentCombination, List<List<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(currentCombination));
            return;
        }
        
        for (int i = start; i < candidates.length && candidates[i] <= target; i++) {
            currentCombination.add(candidates[i]);
            dfs(candidates, target - candidates[i], i, currentCombination, result);
            currentCombination.remove(currentCombination.size() - 1);
        }
    }
}
