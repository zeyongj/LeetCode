class Solution:
    def countTime(self, time: str) -> int:
        h1, h2, _, m1, m2 = time
        if h1 == '?' and h2 == '?':
            hr = 24
        elif h1 == '?':
            hr = 3 if h2 < '4' else 2
        elif h2 == '?':
            hr = 4 if h1 == '2' else 10
        else:
            hr = 1
        mn = (6 if m1 == '?' else 1) * (10 if m2 == '?' else 1)
        return hr * mn