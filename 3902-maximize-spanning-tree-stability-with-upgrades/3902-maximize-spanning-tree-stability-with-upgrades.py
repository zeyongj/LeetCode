class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        initial_uf = UnionFind(n)
        # Observation 1: Find minimum s_i for must-have edges.
        min_s = inf
        for u, v, s, must in edges:
            if not must: continue
            min_s = min(min_s, s)

            # Observation 2: The must-have edges form a cycle.
            if not initial_uf.union(u, v):
                return -1
        
        def check(min_stability: int) -> bool:
            # Observation 1
            if min_stability > min_s:
                return False
            
            # This copies the initial state, where all `must-have edges`
            # are connected.
            uf = UnionFind(n)
            uf.rank, uf.root = initial_uf.rank[:], initial_uf.root[:]

            # Observation 3: List of edges to consider an upgrade
            upgrade = []
            for u, v, s, must in edges:
                if must: continue
                # Observation 3
                if s >= min_stability:
                    uf.union(u, v)
                elif s * 2 >= min_stability:
                    upgrade.append((u, v))

            r = k  # number of upgrades remaining
            # The following edge selection method will not waste our chances to
            # upgrade. See proof below.
            for u, v in upgrade:
                if uf.is_connected(u, v): continue
                if not r: return False
                uf.union(u, v)
                r -= 1
            
            # Observation 3
            return all(uf.find(i) == uf.find(0) for i in range(n))

        left, right = -1, max(s for _, _, s, _ in edges) * 2
        while left < right:
            mid = left + (right - left + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left

class UnionFind:
    def __init__(self, n: int) -> None:
        self.rank = [1] * n
        self.root = [i for i in range(n)]

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_x] = root_y
            self.rank[root_y] += 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)