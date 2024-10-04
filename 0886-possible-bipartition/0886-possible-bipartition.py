class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a,b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        col = [-1]*(n)
        q = deque()

        for i in range(n):
            if (col[i] == -1):
                q.append([i, 0])
                col[i] = 0
            
                while len(q) != 0:
                    v,c = q.popleft()
                    
                    for j in graph[v]:
                        if (col[j] == c):
                            return False
                        if (col[j] == -1):
                            col[j] = 0 if c == 1 else 1
                            q.append([j, col[j]])
        return True