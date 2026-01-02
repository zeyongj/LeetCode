class Solution:
    def maxAbsValExpr(self, xs, ys):
        points = []
        for i, (x, y) in enumerate(zip(xs, ys)):
            points.append((
                x + y + i, 
                x + y - i,
                x - y + i,
                x - y - i
            ))
        return max(max(dim) - min(dim) for dim in zip(*points))