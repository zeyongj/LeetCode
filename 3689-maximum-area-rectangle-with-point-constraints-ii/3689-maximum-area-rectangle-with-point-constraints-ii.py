class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = list(zip(xCoord, yCoord))

        # sort by x, then y
        points.sort()
        yAxis = sorted(set(yCoord))
        yPos = {y: i for i,y in enumerate(yAxis)}
        yMax = {y: -inf for y in yAxis}
        maxTree = SegTree(len(yAxis))
        prevX, prevY = points[0]
        res = -1

        for x,y in points[1:]:
            if prevX == x and yMax[prevY] == yMax[y] \
                and yMax[y] > maxTree.query(yPos[prevY], yPos[y]):
                # x's and y's are aligned
                # and no other points in the rectangle
                res = max(res, (y-prevY) * (x - yMax[y]))

            # update the info of (prevX, prevY)
            yMax[prevY] = prevX
            maxTree.update(yPos[prevY], prevX)
            prevX, prevY = x, y
        return res

class SegTree:

    def __init__(self, n: int):
        self.n = 1<<n.bit_length()
        self.tree = [-inf] * (self.n<<1)

    def update(self, idx: int, val: int):
        idx += self.n
        while idx:
            self.tree[idx] = val
            idx >>= 1

    def query(self, l: int, r: int) -> int:
        res = -inf
        l += self.n
        r += self.n
        while r-l > 1:
            if not l&1:
                res = max(res, self.tree[l+1])
            if r&1:
                res = max(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res