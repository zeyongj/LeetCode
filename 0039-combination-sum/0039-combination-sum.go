import "sort"

func combinationSum(candidates []int, target int) [][]int {
    sort.Ints(candidates)
    result := [][]int{}
    dfs(candidates, target, 0, []int{}, &result)
    return result
}

func dfs(candidates []int, target int, start int, currentCombination []int, result *[][]int) {
    if target == 0 {
        combination := make([]int, len(currentCombination))
        copy(combination, currentCombination)
        *result = append(*result, combination)
        return
    }

    for i := start; i < len(candidates) && candidates[i] <= target; i++ {
        dfs(candidates, target - candidates[i], i, append(currentCombination, candidates[i]), result)
    }
}
