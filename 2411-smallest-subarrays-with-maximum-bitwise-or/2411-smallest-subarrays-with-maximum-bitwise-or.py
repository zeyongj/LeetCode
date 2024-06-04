class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:        

        n, ans, bits = len(nums), deque(), defaultdict(int)

        for i in range(n)[::-1]:               
            I = i

            for b in range(31):
                if nums[i] & (1 << b): bits[b] = i
                elif b in bits and I < bits[b]: I = bits[b] 

            ans.appendleft(I+1-i)

        return list(ans)