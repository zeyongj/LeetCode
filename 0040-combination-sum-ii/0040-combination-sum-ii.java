class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();
        findCombinations(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }
    
    private void findCombinations(int[] candidates, int target, int index, List<Integer> current, List<List<Integer>> res) {
        if(target == 0) {
            res.add(new ArrayList<>(current));
            return;
        }
        if(target < 0) return;
        for(int i = index; i < candidates.length; i++) {
            if(i == index || candidates[i] != candidates[i - 1]) {
                current.add(candidates[i]);
                findCombinations(candidates, target - candidates[i], i + 1, current, res);
                current.remove(current.size() - 1);
            }
        }
    }
}
