from itertools import combinations

class Solution(object):
    def combinationSum3(self, k, n):
        return [
            list(comb) 
            for comb in combinations(range(1, 10), k) 
            if sum(comb) == n
        ]