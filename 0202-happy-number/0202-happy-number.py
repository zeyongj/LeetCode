class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit * digit
            return total_sum
        while n != 1 and n != 4:
            n = get_next(n)
        return n == 1