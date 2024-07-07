class Solution:
    def countEven(self, num: int) -> int:
        ans = sum(1 for x in range(1, num + 1) if sum(int(digit) for digit in str(x)) % 2 == 0)
        return ans
