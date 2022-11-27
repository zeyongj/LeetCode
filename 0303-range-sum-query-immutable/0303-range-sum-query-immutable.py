class NumArray:
    def __init__(self, nums):
        self.arr = [0] + list(accumulate(nums))
        
    def sumRange(self, left, right):
        return self.arr[right + 1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)