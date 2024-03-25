class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            extension = [set + [num] for set in res]
            res.extend(extension)
            # temp = []
            # for set in res:
            #     extension = set + [num]
            #     temp.append(extension)
            # res.extend(temp)
        
        return res