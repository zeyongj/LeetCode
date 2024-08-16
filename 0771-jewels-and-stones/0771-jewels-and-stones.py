class Solution:
    def numJewelsInStones(self, jw: str, st: str) -> int:
        count = 0
        for i in range(len(jw)):
            for j in range(len(st)):
                if jw[i] is st[j]:
                    count += 1
        return count