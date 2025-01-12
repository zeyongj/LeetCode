class Solution:
    def canBeValid(self, s, locked):
        if len(s) % 2 != 0:
            return False

        open_possible = close_possible = 0

        # Left to right pass
        for i in range(len(s)):
            open_possible += 1 if locked[i] == '0' or s[i] == '(' else -1
            if open_possible < 0:
                return False

        # Right to left pass
        for i in range(len(s) - 1, -1, -1):
            close_possible += 1 if locked[i] == '0' or s[i] == ')' else -1
            if close_possible < 0:
                return False

        return True