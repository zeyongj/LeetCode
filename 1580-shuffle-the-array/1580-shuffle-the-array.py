class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        res = []
        for i in range(2*n):
            if i%2 == 0:
                res.append(x[i//2])
            else:
                res.append(y[i//2])
        return res