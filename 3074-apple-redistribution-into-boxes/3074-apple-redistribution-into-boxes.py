class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        az=sum(apple)
        for i, x in enumerate(sorted(capacity, reverse=True)):
            az-=x
            if az<=0: return i+1
        return -1
        