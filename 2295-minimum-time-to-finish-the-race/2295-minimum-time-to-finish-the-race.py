class Solution:
    def minimumFinishTime(self, T, c, k):
        f = [ 10**9 for _ in range(k + 1) ]
        for t in T:
            lap_time = t[0]
            tot_time = t[0]
            for i in range(1, k + 1):
                f[i] = min(f[i], tot_time)
                lap_time *= t[1]
                tot_time += lap_time
                if tot_time > 10**9:
                    break
        for i in range(2, k + 1):
            for j in range(1, i):
                f[i] = min(f[i], f[j] + c + f[i - j])
        return f[k]