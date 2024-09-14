class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        m, res = {}, [0] * len(arr)
        for i, v in enumerate(arr):
            if v not in m: m[v] = list()
            m[v].append(i)

        for x in m:
            l = m[x]
            pre = [0] * (len(l) + 1)
            for i in range(len(l)):
                pre[i + 1] = pre[i] + l[i]
            for i, v in enumerate(l):
                res[v] = (v * (i + 1) - pre[i + 1]) + ((pre[len(l)] - pre[i]) - v * (len(l) - (i)))
        return res