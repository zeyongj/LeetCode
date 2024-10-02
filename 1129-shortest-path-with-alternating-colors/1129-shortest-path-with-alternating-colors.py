class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        redChild=defaultdict(set)
        blueChild=defaultdict(set)
        for s,d in redEdges:
            redChild[s].add(d)
        for s,d in blueEdges:
            blueChild[s].add(d)
        answer=[-1]*n
        answer[0]=0
        queue=deque() # (node,previous_edge_color) / previous_edge_color=1 if previous edge is Blue else previous_edge_color=0
        queue.append((0,1))
        queue.append((0,0))
        c=0
        visited=set()
        while(queue):
            c+=1
            for i in range(len(queue)):
                node,previous_edge_color=queue.popleft()
                if previous_edge_color:
                    for child in redChild[node]:
                        if answer[child]==-1:
                            answer[child]=c
                        if (child,0) not in visited:
                            queue.append((child,0))
                            visited.add((child,0))
                else:
                    for child in blueChild[node]:
                        if answer[child]==-1:
                            answer[child]=c
                            
                        if (child,1) not in visited:
                            queue.append((child,1))
                            visited.add((child,1))
        return answer