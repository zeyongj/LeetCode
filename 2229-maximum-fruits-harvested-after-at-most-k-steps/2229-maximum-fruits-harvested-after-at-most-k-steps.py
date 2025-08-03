class Solution:
    def maxTotalFruits(self, A: List[List[int]], pos: int, k: int) -> int:
            amt = {}
            for a, b in A:
                amt[a] = b
                
            # Every position with fruit except the start position.
            position = [a for a, b in A if a != pos]
            lft, rgt, n = [], [], len(position)
        
            idx = bisect.bisect_right(position, pos)
            
            # Right pre-sum
            cur_f = 0
            for i in range(idx, n):
                cur_pos = position[i]
                cur_f += amt[cur_pos]
                rgt.append([cur_pos - pos, cur_f])
            
            # Left pre-sum
            cur_f = 0
            for i in range(idx - 1, -1, -1):
                cur_pos = position[i]
                cur_f += amt[cur_pos]
                lft.append([pos - cur_pos, cur_f])
            
            # Go right then turn left
            ans = 0
            for r_dist, r_f in rgt:
                if r_dist <= k:
                    cur_f = r_f
                    l_dist = k - 2 * r_dist
                    if l_dist > 0:             # Check fruit collected from the left side.
                        idx = bisect.bisect_right(lft, [l_dist, float('inf')])
                        if idx > 0:
                            cur_f += lft[idx - 1][1]
                    ans = max(ans, cur_f)
            
            # Go left then turn right
            for l_dist, l_f in lft:
                if l_dist <= k:
                    cur_f = l_f
                    r_dist = k - 2 * l_dist
                    if r_dist > 0:             # Check fruit collected from the right side.
                        idx = bisect.bisect_right(rgt, [r_dist, float('inf')])
                        if idx > 0:
                            cur_f += rgt[idx - 1][1]
                    ans = max(ans, cur_f)

            return ans + amt.get(pos, 0)       # Add fruit collected at the start position.