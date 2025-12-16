
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj_list = defaultdict(list)
        for h in hierarchy:
            adj_list[h[0] - 1].append(h[1] - 1)
        
        @lru_cache(None)
        def dfs(employee, has_discount):
            cost = present[employee] // 2 if has_discount else present[employee]
            profit = future[employee] - cost
            
            buy_current = {cost: profit} if cost <= budget else {}
            skip_current = {0: 0}
            
            for child in adj_list[employee]:
                child_with_discount = dfs(child, True) # Do something
                child_no_discount = dfs(child, False) # Do nothing
                
                new_buy = {}
                for spent, prof in buy_current.items(): # Do something, but the current stock
                    for child_spent, child_prof in child_with_discount.items():
                        total_spent = spent + child_spent
                        if total_spent <= budget:
                            total_prof = prof + child_prof
                            if total_spent not in new_buy or new_buy[total_spent] < total_prof:
                                new_buy[total_spent] = total_prof
                buy_current = new_buy # This is mandatory because you need to check 
                                      # all possible combinations of picking children results. 
                                      # For example if the given graph is 1 -> 2, and 1 -> 3, 
                                      # it might be correct to either pick the path from 1 to 2, 
                                      # the path 1 to 3, or both paths if there is still budget left. 
                                      # Same goes for a skipping action.
                
                new_skip = {}
                for spent, prof in skip_current.items(): # Do nothing, skip the current stock
                    for child_spent, child_prof in child_no_discount.items():
                        total_spent = spent + child_spent
                        if total_spent <= budget:
                            total_prof = prof + child_prof
                            if total_spent not in new_skip or new_skip[total_spent] < total_prof:
                                new_skip[total_spent] = total_prof
                skip_current = new_skip
            
            result = {} # Merge the results of doing something and doing nothing at node employee
            for spent, prof in buy_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            for spent, prof in skip_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            
            return result
        
        result = dfs(0, False)
        return max(result.values()) if result else 0