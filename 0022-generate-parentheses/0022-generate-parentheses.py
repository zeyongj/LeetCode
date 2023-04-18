class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate("", n, 0, 0, result)
        return result
    
    def generate(self, current: str, n: int, open: int, close: int, result: List[str]):
        if open == n and close == n:
            result.append(current)
            return
        
        if open < n:
            self.generate(current + "(", n, open+1, close, result)
        
        if close < open:
            self.generate(current + ")", n, open, close+1, result)
