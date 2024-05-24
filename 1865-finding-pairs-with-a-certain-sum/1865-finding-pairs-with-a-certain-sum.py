import collections
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.count1 = collections.Counter(self.nums1)
        self.count2 = collections.Counter(self.nums2)
        

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        self.nums2[index] += val
        cur = self.nums2[index]
        
        self.count2[prev] -= 1
        self.count2[cur] += 1
        

    def count(self, tot: int) -> int:
        count = 0
        
        for key, val in self.count1.items():
            diff = tot - key
            if diff in self.count2:
                count += val * self.count2[diff]
                
        return count
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)