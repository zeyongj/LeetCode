class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        
        # Iterate over numbers 1 to 9
        for i in range(1, 10):
            self.dfs(i, n, result)
        
        return result
    
    # Helper DFS function
    def dfs(self, curr: int, n: int, result: List[int]):
        if curr > n:
            return  # Stop recursion if current number is greater than n
        result.append(curr)  # Add current number to result
        
        # Try appending digits 0-9 to the current number
        for i in range(10):
            if curr * 10 + i > n:
                return  # Stop if the next number exceeds n
            self.dfs(curr * 10 + i, n, result)  # Recursive DFS
