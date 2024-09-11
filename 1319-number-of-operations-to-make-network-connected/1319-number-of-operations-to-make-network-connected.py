class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #check if possible , should have atleast n-1 edges
        if(len(connections) < n-1 ):
            return -1 

        #build adjacency list, bidirectional edges
        graph = { i:[] for i in range(0,n)}
        for item in connections:
            graph[item[0]].append(item[1])
            graph[item[1]].append(item[0])

        # find number of connected components using bfs 
        visited = [ 0 for _ in range(0,n)]
        comp_count = 0 # number of connected components
        for i in range(0,n):
            if(visited[i]==0 ):
                visited[i] = 1
                comp_count += 1
                dq = deque([i]);
                while(len(dq)>0):
                    curNode = dq.popleft();
                    for item in graph[curNode]:
                        if(visited[item] == 0 ):
                            visited[item] = 1
                            dq.append(item);

        return comp_count-1
