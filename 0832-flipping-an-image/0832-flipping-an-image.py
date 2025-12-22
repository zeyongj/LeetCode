class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in image:
            i.reverse()
            res.append([x ^ 1 for x in i])
        return res