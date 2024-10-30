class Solution :
    def find(self,u,parent):
        if u==parent[u]:
            return u
        return self.find(parent[u],parent)

    def unionDSU(self,u,v,parent) :
        p1=self.find(u,parent)
        p2=self.find(v,parent)
        parent[p2]=p1

    def mst(self,k,edges,includeEdge,excludeEdge) :
        n=len(includeEdge)
        m=len(excludeEdge)
        parent=[]
        for i in range(k): 
            parent.append(i);
        
        res=0
        count=0

        if n!= 0 :
            self.unionDSU(includeEdge[0], includeEdge[1], parent)
            res+=includeEdge[2]
            count+=1
        
        for edge in edges:
            u=edge[0];
            v=edge[1];
            cost=edge[2];

            if m!=0 and excludeEdge[0]==u and excludeEdge[1]==v and excludeEdge[2]==cost :
                continue
            
            if n!=0 and includeEdge[0]==u and includeEdge[1]==v and includeEdge[2]==cost :
                continue
            
            p1=self.find(u,parent)
            p2=self.find(v,parent)

            if p1!= p2:
                self.unionDSU(p1, p2, parent)
                res+= cost
                count += 1
                    
        return  res if count==k-1 else float('inf')
    
    def findCriticalAndPseudoCriticalEdges(self, k:int, edges:List[List[int]]) -> List[List[int]]:
        
        originalEdges=[]
        for edge in edges : 
            originalEdge=[edge[0],edge[1],edge[2]]
            originalEdges.append(originalEdge)
            
        X=len(originalEdges)
        ans=[]
        criticalEdges=[]
        pseudoCriticalEdges=[]

        
        edges=sorted(edges, key = lambda x: x[2])

        emptyVector=[]
        originalCost = self.mst(k, edges, emptyVector, emptyVector)
        
        for i in range(X): 
            excludedCost = self.mst(k, edges, emptyVector, originalEdges[i])
            includedCost = self.mst(k, edges, originalEdges[i], emptyVector)

            if excludedCost > originalCost :
                criticalEdges.append(i)
                
            elif includedCost==originalCost : 
                pseudoCriticalEdges.append(i)
                    
        ans.append(criticalEdges)
        ans.append(pseudoCriticalEdges)
        return ans