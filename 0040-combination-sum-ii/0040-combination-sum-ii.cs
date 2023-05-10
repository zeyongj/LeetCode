public class Solution {
    public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
        Array.Sort(candidates);
        var result = new List<IList<int>>();
        CombinationSum2(candidates, target, 0, new List<int>(), result);
        return result;
    }

    private void CombinationSum2(int[] candidates, int target, int start, List<int> combination, IList<IList<int>> result) {
        if (target == 0) {
            result.Add(new List<int>(combination));
            return;
        }

        for (int i = start; i < candidates.Length && candidates[i] <= target; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue; // skip duplicates

            combination.Add(candidates[i]);
            CombinationSum2(candidates, target - candidates[i], i + 1, combination, result);
            combination.RemoveAt(combination.Count - 1); // remove last element
        }
    }
}
