class Solution(object):
    def canReorderDoubled(self, arr):
        cnt = Counter(arr)
        arr.sort()
        for x in arr:
            if cnt[x] == 0: continue
            if x < 0 and x % 2 != 0: return False  # For example: arr=[-5, -2, 1, 2], x = -5, there is no x/2 pair to match
            y = x * 2 if x > 0 else x // 2
            if cnt[y] == 0: return False  # Don't have the corresponding `y` to match with `x` -> Return IMPOSSIBLE!
            cnt[x] -= 1
            cnt[y] -= 1
        return True