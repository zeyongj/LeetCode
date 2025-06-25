class Solution:
    from collections import Counter
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=Counter(nums)
        for i in a:
            if a[i]>1:
                return True
        return False
                
        