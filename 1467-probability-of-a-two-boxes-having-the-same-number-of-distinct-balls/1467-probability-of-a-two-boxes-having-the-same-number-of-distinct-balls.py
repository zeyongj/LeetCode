class Solution:
    def getProbability(self, balls: List[int]) -> float:
        allComb = comb(sum(balls),sum(balls)//2)
        @lru_cache(None)
        #num of unique balls in boxA-boxB, num of total balls in boxA, num of total balls in boxB, current bucket
        def helper(offset,num1,num2,idx):
            if idx==-1:
                return num1==num2==offset==0
            res = 0
            for k in range(1,balls[idx]):
                res+=helper(offset,num1-balls[idx]+k,num2-k,idx-1)*comb(balls[idx],k)
            res+=helper(offset-1,num1-balls[idx],num2,idx-1)
            res+=helper(offset+1,num1,num2-balls[idx],idx-1)
            return res
        return helper(0,sum(balls)//2,sum(balls)//2,len(balls)-1)/allComb