class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
 
        n, sm, acc, cnt, ans = len(nums), sum(nums), 0, 0, []
        
        d = target//sm * n
        target%= sm
       
        nums.extend(nums)

        for i, num in enumerate(nums):

            while num > target - acc:
                acc-= nums[i - cnt]
                cnt-= 1

            acc+= num
            cnt+= 1

            if acc == target:
                ans.append(cnt + d)

        return min(ans, default = -1)