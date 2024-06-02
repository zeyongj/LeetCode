class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        
        nodes = Counter(chain(*edges))
        nodes = {i:nodes[i] if i in nodes else 0 for i in range(1, n+1)}
        edges = Counter(map(lambda x:(min(x), max(x)), edges))
        
        n = 2 + 2*max(nodes.values())
        ans, ctr = [0] * n, Counter(nodes.values())

        for c1, c2 in list(product(ctr, ctr)):
            if c1 > c2: continue
            ans[c1+c2] += ctr[c1]*ctr[c2] if c1!=c2 else ctr[c1]*(ctr[c2]-1)//2

        for i, j in edges:
            sm = nodes[i] + nodes[j]
            ans[sm] -= 1
            ans[sm - edges[(i,j)]]+= 1

        ans = list(accumulate(ans[::-1]))[::-1]

        return [ans[min(q+1, n-1)] for q in queries] 