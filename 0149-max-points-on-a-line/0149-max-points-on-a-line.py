class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points) #amount of point
        maxP = 0 # current max points - initalize variable

        for i in range(n):
            X = points[i][0]
            Y = points[i][1]
            map = {} # create temperory dict for story points

            for j in range(i+1, n):
                dx = points[j][0] - X
                dy = points[j][1] - Y # change in x and y pos

                if(dx != 0): 
                    d = dy/dx
                    if d in map:
                        map[d] = map[d] + 1
                    else:
                        map[d] = 1 
                else:
                    if 20001.0 in map:
                        map[20001.0] = map[20001.0] + 1
                    else:
                        map[20001.0] = 1 # test case put here since I cant solve

            if map:
                maxP = max(maxP, max(map.values())) # return longest one by sorting it and get the max - since you have to get the value (sort by value), I don't know how to do max() with it

        return maxP + 1