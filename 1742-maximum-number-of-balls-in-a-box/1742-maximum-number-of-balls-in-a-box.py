class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxNumber2Cnt = {}
        maxBall = 0
        for i in range(lowLimit, highLimit + 1):
            boxNumber = self.sumOfNumChar(i)
            boxNumber2Cnt[boxNumber] = boxNumber2Cnt.get(boxNumber, 0) + 1
            maxBall = max(maxBall, boxNumber2Cnt[boxNumber])
        return maxBall
    
    def sumOfNumChar(self, num: int) -> int:
        ans = 0
        while num != 0:
            ans += num % 10
            num = num // 10
        return ans