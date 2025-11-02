class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def idx(r, c):
            return r*n+c
        d=(0, 1, 0,-1, 0)
        def cross(r, c):
            nonlocal comp
            for a in range(4):
                di, dj=d[a], d[a+1]
                i, j=r+di, c+dj
                while True:
                    pos=idx(i, j)
                    if i<0 or i>=m or j<0 or j>=n or grid[pos]=='X':
                        break
                    comp-=grid[pos]==' '
                    grid[pos]='V'
                    i+=di
                    j+=dj
        comp=m*n
        grid=[' ']*(m*n)

        for ij in walls:
            grid[idx(ij[0], ij[1])]='X'
            comp-=1
        for ij in guards:
            grid[idx(ij[0], ij[1])]='X'
            comp-=1
        for ij in guards:
            cross(ij[0], ij[1])
        return comp             