class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def count_up_to(x):
            num = str(x)

            @cache
            def dfs(pos, tight, sum_digits, prod_digits):
                if pos == len(num):
                    return 1 if sum_digits and prod_digits % sum_digits == 0 else 0

                up = int(num[pos]) if tight else 9
                count = 0

                for digit in range(up + 1):
                    new_sum = sum_digits + digit
                    new_prod = 1 if new_sum == 0 else prod_digits * digit # don't set prod=0 if we are in leading 0s.
                    count += dfs(pos + 1, tight and digit == up, new_sum, new_prod)

                return count
            return dfs(0, True, 0, 1)

        return count_up_to(r) - count_up_to(l - 1)