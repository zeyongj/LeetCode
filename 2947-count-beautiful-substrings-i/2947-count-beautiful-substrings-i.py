class Solution:
  def beautifulSubstrings(self, s: str, k: int) -> int:
    cnt_0 = [0] * (len(s) + 1)
    cnt_1 = [0] * (len(s) + 1)
    for i, c in enumerate(s):
      if c in ['a', 'e', 'i', 'o', 'u']:
        cnt_0[i + 1] = cnt_0[i] + 1
        cnt_1[i + 1] = cnt_1[i]
      else:
        cnt_0[i + 1] = cnt_0[i]
        cnt_1[i + 1] = cnt_1[i] + 1

    res = 0
    for i in range(len(s)):
      for j in range(i + 1, len(s) + 1):
        v1, v2 = cnt_0[j] - cnt_0[i], cnt_1[j] - cnt_1[i]
        if v1 == v2 and v1 * v2 % k == 0:
          res += 1
    return res