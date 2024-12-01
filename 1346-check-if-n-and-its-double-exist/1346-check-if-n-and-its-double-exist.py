class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}  

        for num in arr: 
            if (2 * num in seen) or (num % 2 == 0 and num // 2 in seen):
                return True  
            seen[num] = seen.get(num, 0) + 1

        return False  