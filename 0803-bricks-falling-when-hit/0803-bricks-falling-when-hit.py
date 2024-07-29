class UnionFind:
    def __init__(self):

        self.father = {}
        self.block_count = 0
        self.size_of_set = {}
    
    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.block_count += 1
        self.size_of_set[x] = 1
    
    def find(self, x):
        root = x
        while self.father[root]:
            root = self.father[root]
        
        while x != root:
            old_father = self.father[x]
            self.father[x] = root
            x = old_father
        return root
    
    def merge(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.father[fa] = fb
            self.block_count -= 1
            self.size_of_set[fb] += self.size_of_set[fa]
    
    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def num_block(self):
        return self.block_count
    
    def get_size_of_set(self, x) -> int:
        root = self.find(x)
        size = self.size_of_set[root]
        return size

class Solution:

    def isValid(self, x, y, grid):
        rows = len(grid)
        cols = len(grid[0])
        if 0 <= x < rows and 0 <= y < cols:
            return True
        return False
    
    def mergeNeighbors(self, i, j, grid, uf):
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in DIRECTIONS:
            x, y = i+dx, j+dy
            if self.isValid(x, y, grid) and grid[x][y] == 1:
                uf.merge((i, j),(x, y))
        if i == 0:
            uf.merge((i, j), -100)

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        # iterate through hits
        for x, y in hits:
            grid[x][y] -= 1
        
        uf = UnionFind()
        WALL = -100
        uf.add(WALL)
        # connect the 1 on first row to "WALL"
        for j in range(cols):
            if grid[0][j] == 1:
                uf.add((0, j))
                uf.merge(WALL, (0, j))
        
        # add all 1's into uf
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    uf.add((i, j))
        
        # connect all connected 1's
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.mergeNeighbors(i, j, grid, uf)
        
        ans = [0 for _ in range(len(hits))]
        # print(uf.father)
        # print(uf.get_size_of_set(WALL))
        for index in range(len(hits)-1, -1, -1):
            i, j = hits[index]
            grid[i][j] += 1
            after = uf.get_size_of_set(WALL)

            if grid[i][j] != 1:
                # indication that nothing falls off
                ans[index] = 0
                continue
            # put i, j back in
            uf.add((i, j))
            self.mergeNeighbors(i, j, grid, uf)
            before = uf.get_size_of_set(WALL)
            # since the one erased does not count
            ans[index] = before - after
            if ans[index] != 0:
                ans[index] -= 1
            # print(uf.father)
            # print(uf.get_size_of_set(WALL))
        
        return ans