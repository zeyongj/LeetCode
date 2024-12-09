class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        count = 0
        done = {tuple(cells) : 0}
        def trans():
            nonlocal cells
            tmp = [0]*8
            for i in range(1,7):
                if cells[i-1] == cells[i+1]:
                    tmp[i] = 1
            cells = tmp.copy()
        lcount = None
        for i in range(n):
            trans()
            count += 1
            if tuple(cells) in done:
                lcount = done[tuple(cells)]
                break
                
            else:
                done[tuple(cells)] = count
        if lcount == None: return cells
        time = (n-count)%(count-lcount)
        for i in range(time):
            trans()
        return cells