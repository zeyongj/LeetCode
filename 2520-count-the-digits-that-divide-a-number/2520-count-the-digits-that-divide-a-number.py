class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for i in str(num):
            if int(num)%int(i) == 0:
                count = count+1
        return count