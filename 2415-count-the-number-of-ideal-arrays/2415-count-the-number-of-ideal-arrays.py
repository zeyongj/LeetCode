from math import comb

MOD = 10**9 + 7
MAX = 10001
cnt = [[0] * 14 for _ in range(MAX)]
comb_table = [[0] * 14 for _ in range(MAX)]

# Precompute combinations
for s in range(MAX):
    for r in range(min(s, 13) + 1):
        comb_table[s][r] = comb(s, r)

# Sieve-like DP for count
for div in range(1, MAX):
    cnt[div][0] += 1
    for i in range(div * 2, MAX, div):
        for bars in range(13):
            if cnt[div][bars]:
                cnt[i][bars + 1] += cnt[div][bars]

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        res = 0
        for i in range(1, maxValue + 1):
            for bars in range(min(14, n)):
                res = (res + cnt[i][bars] * comb_table[n - 1][bars]) % MOD
        return res