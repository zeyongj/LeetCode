class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        one=two=float("inf")
        for i in prices:
            if i<one:
                one,two=i,one
            else:
                two=min(two,i)
        if money>=(one+two):
            return money-one-two
        return money