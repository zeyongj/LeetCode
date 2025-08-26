class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return (it:=max(dimensions, key=lambda r:(r[0]**2+r[1]**2, r[0]*r[1]))) and it[0]*it[1]
        
        