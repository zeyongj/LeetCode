class Solution(object):
    def maximumBeauty(self, items, queries):
        items.sort()
        ans, beauty = [], [items[0][1]] * len(items)
        for i in range(1, len(items)): beauty[i] = max(beauty[i - 1], items[i][1])

        def bs(t):
            ans, s, e = 0, 0, len(items) - 1
            while s <= e:
                m = (s + e) // 2
                if items[m][0] <= t:
                    ans = beauty[m]
                    s = m + 1
                else: e = m - 1
            return ans

        for i in queries: ans.append(bs(i))
        return ans