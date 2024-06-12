class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted(flowers, key=lambda x:x[0])
        end = sorted(flowers, key=lambda x:x[1])
        ans = []
        for man in people:
            i = bisect_left(end, man, key=lambda x:x[1])
            j = bisect_right(start, man, key=lambda x:x[0])
            ans.append(j - i)

        return ans 