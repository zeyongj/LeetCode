class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        
        s = set()
        
        for i,j in coordinates:
            
            s.add((i,j))
        
        vis = set()
        ans = [0 for i in range(5)] 

        for i,j in coordinates:
            if (i,j,i+1,j+1) not in vis and i+1<m and j+1<n:
                blocks = 1
                if (i+1,j+1) in s and i+1<m and j+1<n:
                    blocks+=1
                if (i+1,j) in s and i+1<m:
                    blocks+=1
                if (i,j+1) in s and j+1<n:
                    blocks+=1
                ans[blocks]+=1
                vis.add((i,j,i+1,j+1))
            if (i-1,j,i,j+1) not in vis and i-1>=0 and j+1<n:
               
                blocks = 1
                if (i-1,j) in s and i-1>=0:
                    blocks+=1
                if (i,j+1) in s and j+1<n:
                    blocks+=1
                if (i-1,j+1) in s and i-1>=0 and j+1<n:
                    blocks+=1
                ans[blocks]+=1
                vis.add((i-1,j,i,j+1))
                
            if (i-1,j-1,i,j) not in vis and i-1>=0 and j-1>=0:
                blocks = 1
                if (i-1,j-1) in s and i-1>=0 and j-1>=0:
                    blocks+=1
                if (i-1,j) in s and i-1>=0:
                    blocks+=1
                if (i,j-1) in s and j-1>=0:
                    blocks+=1
                ans[blocks]+=1
                vis.add((i-1,j-1,i,j))
            if (i,j-1,i+1,j) not in vis and j-1>=0 and i+1<m:
                blocks = 1
                if (i,j-1) in s and j-1>=0:
                    blocks+=1
                if (i+1,j-1) in s and i+1<m and j-1>=0:
                    blocks+=1
                if (i+1,j) in s and i+1<m:
                    blocks+=1
                ans[blocks]+=1
                vis.add((i,j-1,i+1,j))
        ans [0] = (m-1)*(n-1)-sum(ans)
        return ans