class Solution:
    def bestClosingTime(self, customers: str) -> int:

        x = y = z = 0
        
        for i, ch in enumerate(customers):
            z += 1 if ch == "Y" else -1
            if z > y:
                y, x = z, i + 1 
                
        return x
                