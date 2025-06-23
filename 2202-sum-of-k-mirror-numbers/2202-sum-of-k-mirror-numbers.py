class Solution:
    # building 1st half (pre) + 2nd half
    def solve(self, pre, is_odd):
        tmp = pre
        if is_odd:
            tmp //= 10

        while tmp > 0:
            pre = pre * 10 + (tmp % 10)  # 11 + 3 => 113? // 11*10 + 3 = 113
            tmp //= 10

        return pre

    # this will generate all palindrome for a given length
    def kthPalindrome(self, length):
        ans = []

        # 1st half length
        half = (length + 1) // 2 - 1
        mn, mx = 1, 9
        for _ in range(half):
            mn *= 10
            mx = mx * 10 + 9

        val = 0
        while True:
            pos = val
            num = mn + pos
            if num > mx:
                break
            else:
                complete = self.solve(num, length % 2)
                ans.append(complete)
            val += 1

        return ans

    def is_palin(self, num, base):
        # convert to base
        s = ""
        while num > 0:
            s += chr((num % base) + ord('0'))
            num //= base

        # Check if s is a palindrome
        return s == s[::-1]

    def kMirror(self, k: int, n: int) -> int:
        sum_ = 0
        cnt = 0

        for length in range(1, 12):
            ele = self.kthPalindrome(length)

            for val in ele:
                if self.is_palin(val, k):
                    sum_ += val
                    cnt += 1
                    if cnt == n:
                        return sum_

        return sum_