# Cache all prime numbers
N = 5 * (10 ** 4) + 1
seive = [True] * (N)
seive[0] = seive[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if not seive[i]: continue
    for j in range(i*i, N, i):
        seive[j] = False


class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        maxval = deque([])
        minval = deque([])
        plist = deque([])

        l, cnt = 0, 0
        for r, x in enumerate(nums):
            if seive[x]:
                # Add to order of occurence list
                plist.append(r)
                
                # Add to max monotonic queue
                while maxval and x > nums[maxval[-1]]:
                    maxval.pop()
                maxval.append(r)
                
                # Add to min monotonic queue
                while minval and x < nums[minval[-1]]:
                    minval.pop()
                minval.append(r)

                # If window is not valid start moving the left pointer to shrink size
                while len(plist) >= 2 and maxval and minval and nums[maxval[0]] - nums[minval[0]] > k:
                    if seive[nums[l]]:
                        plist.popleft() 
                        if maxval[0] == l:
                            maxval.popleft()
                        if minval[0] == l:
                            minval.popleft()
                    l += 1

            # If there are at least 2 prime numbers and the window is valid
            # then add all maximum number of subarray possible using order
            # of occurence list
            if len(plist) >= 2 and nums[maxval[0]] - nums[minval[0]] <= k:
                index = plist[-2]
                cnt += (index - l + 1)
                    
        return cnt