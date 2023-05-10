//import "sort"

func combinationSum2(candidates []int, target int) [][]int {
    sort.Ints(candidates)
    var result [][]int
    backtrack(candidates, target, 0, []int{}, &result)
    return result
}

func backtrack(candidates []int, target int, start int, path []int, result *[][]int) {
    if target == 0 {
        // Make a deep copy of the result and append to the list.
        tmp := make([]int, len(path))
        copy(tmp, path)
        *result = append(*result, tmp)
        return
    }
    
    for i := start; i < len(candidates); i++ {
        // If the current candidate is greater than the target, break the loop.
        if candidates[i] > target {
            break
        }
        // If the current candidate is the same as the previous one, skip it.
        if i > start && candidates[i] == candidates[i - 1] {
            continue
        }
        // Include the candidate in the path.
        path = append(path, candidates[i])
        // Recurse, reducing the target by the chosen candidate's value.
        backtrack(candidates, target - candidates[i], i + 1, path, result)
        // Exclude the candidate from the path.
        path = path[:len(path) - 1]
    }
}
