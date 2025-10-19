class Solution:
    def slowestKey(self, times: List[int], keys: str) -> str:
        mxx, res = times[0], keys[0]
        for i in range(1, len(times)):
            curr = times[i] - times[i - 1]
            if curr > mxx or curr == mxx and keys[i] > res:
                res, mxx = keys[i], curr
        return res