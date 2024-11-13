class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        d = defaultdict(int)
        ans = 0
        l = numWanted
        for i, j in sorted(list(zip(values, labels)), reverse = True):
            if(d[j] < useLimit and l):
                l -= 1
                d[j] += 1
                ans += i
        return ans