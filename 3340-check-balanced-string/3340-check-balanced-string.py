class Solution:
    def isBalanced(self, num: str) -> bool:
        ev_sum=0
        od_sum=0
        for i in range(len(num)):
            if i%2==0:
                ev_sum+=int(num[i])
            else:
                od_sum+=int(num[i])           
        return ev_sum==od_sum