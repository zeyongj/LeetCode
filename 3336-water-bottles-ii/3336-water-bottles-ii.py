from math import sqrt

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numBottles -= 1
        D = (2 * numExchange - 3)**2 + 8 * numBottles
        res = int((-(2 * numExchange - 3) + sqrt(D)) / 2)
        return numBottles + res + 1