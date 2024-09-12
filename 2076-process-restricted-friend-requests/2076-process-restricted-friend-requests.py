class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parents = [i for i in range(n)]
        ranks = [0] * n
        forbidden = collections.defaultdict(set)
        for i, j in restrictions:
            forbidden[i].add(j)
            forbidden[j].add(i)
        
        def find(i):
            if i != parents[i]:
                parents[i] = find(parents[i])
            return parents[i]
        
        def union(p1, p2):
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p1] < ranks[p2]:
                parents[p1] = p2
                p1, p2 = p2, p1
            else:
                ranks[p1] += 1
                parents[p2] = p1
                
            forbidden[p1] |= forbidden[p2]
            for i in forbidden[p2]:
                forbidden[i].remove(p2)
                forbidden[i].add(p1)
            del forbidden[p2]
        
        ans = []
        for i, j in requests:
            p1 = find(i)
            p2 = find(j)
            if p1 == p2:
                ans.append(True)         
            elif p2 in forbidden[p1]:
                ans.append(False)
            else:
                union(p1, p2)
                ans.append(True)

        return ans