/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let result = [];
    let currentCombination = [];
    
    candidates.sort((a, b) => a - b);
    dfs(candidates, target, 0, currentCombination, result);
    
    return result;
};

var dfs = function(candidates, target, start, currentCombination, result) {
    if (target === 0) {
        result.push(Array.from(currentCombination));
        return;
    }
    
    for (let i = start; i < candidates.length && candidates[i] <= target; i++) {
        currentCombination.push(candidates[i]);
        dfs(candidates, target - candidates[i], i, currentCombination, result);
        currentCombination.pop();
    }
};
