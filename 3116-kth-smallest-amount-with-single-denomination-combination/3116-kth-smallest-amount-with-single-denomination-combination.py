class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
                    
        l = 0
        r = 10**18

        n = len(coins)

        def check(x):
            count = 0
            for mask in range(1<<n):
                cnt = 0
                lcm = 0 
                c = []
                for i in range(n):
                    if (mask>>i)&1:
                        cnt+=1 
                        c.append(coins[i])

                lcm = math.lcm(*c)

                if lcm and cnt&1: 
                    count += x//lcm 
                elif cnt%2==0 and lcm and cnt: 
                    count -= x//lcm

            return count>=k


        while l+1<r:
            m = (l+r)>>1

            if check(m):
                r = m 
            else: 
                l = m

        return r
