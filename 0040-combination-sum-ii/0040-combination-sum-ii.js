/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    candidates.sort((a, b) => a - b);
    const result = [];
    backtrack(candidates, target, 0, [], result);
    return result;
};

function backtrack(candidates, target, start, path, result) {
    if (target === 0) {
        result.push([...path]);
        return;
    }

    for (let i = start; i < candidates.length; i++) {
        if (candidates[i] > target) break;

        // Skip the same number after the first one to avoid duplicates
        if (i > start && candidates[i] === candidates[i - 1]) continue;

        path.push(candidates[i]);
        backtrack(candidates, target - candidates[i], i + 1, path, result);
        path.pop();
    }
}
