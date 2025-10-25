class Solution:
    def totalMoney(self, n: int) -> int:
        def arithmeticProgression(leading, last, terms):
            return (leading+last)*terms//2
        q, r= divmod(n, 7)
        return arithmeticProgression(28, 28+(q-1)*7, q)+arithmeticProgression(q+1, q+r, r)
        