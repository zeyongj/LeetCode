import numpy as np

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    
        if len(original) != m * n:
            return []  
        
        # Use NumPy to reshape the 1D array into a 2D array
        arr2D = np.array(original).reshape(m, n)
        return arr2D.tolist()  