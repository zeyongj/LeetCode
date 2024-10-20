from bisect import bisect_left
from random import randint

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.res = []
        self.tot = 0
        self.dic = {}
        for a, b, c, d in rects:
            area = (c - a + 1) * (d - b + 1)
            self.tot += area
            self.res.append(self.tot)
            self.dic[self.tot] = [a, b, c, d]

    def pick(self) -> List[int]:
        random = randint(1, self.tot)
        idx = bisect_left(self.res, random)
        a, b, c, d = self.dic[self.res[idx]]
        return [randint(a, c), randint(b, d)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()