class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            temp = []
            for set in res:
                extention = set + [num]
                temp.append(extention)
            res.extend(temp)
        
        return res