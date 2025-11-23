class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        n = len(skill)
        time = [0] * n

        for x in mana:
            time[0] = time[0] + skill[0] * x
            for i in range(1, n):
                time[i] = max(time[i], time[i - 1]) + skill[i] * x
            for i in range(n - 2, -1, -1):
                time[i] = time[i + 1] - skill[i + 1] * x

        return time[-1]