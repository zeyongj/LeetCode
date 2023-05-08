from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, current_combination, result):
            if target == 0:
                result.append(list(current_combination))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                
                current_combination.append(candidates[i])
                dfs(candidates, target - candidates[i], i, current_combination, result)
                current_combination.pop()

        candidates.sort()
        result = []
        dfs(candidates, target, 0, [], result)
        
        return result
