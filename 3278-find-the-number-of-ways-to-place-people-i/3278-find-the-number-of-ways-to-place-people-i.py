class Solution:
    def numberOfPairs(self, v):
        n = len(v)
        ans = 0

        for i in range(n):
            x1, y1 = v[i][0], v[i][1]

            for j in range(n):
                if i == j:
                    continue

                x2, y2 = v[j][0], v[j][1]
                f = 0

                if y1 >= y2 and x1 <= x2:
                    for k in range(n):
                        if k == i or k == j:
                            continue

                        x3, y3 = v[k][0], v[k][1]

                        if x3 >= x1 and x3 <= x2 and y3 >= y2 and y3 <= y1:
                            f = 1
                            break

                    if f == 0:
                        ans += 1

        return ans