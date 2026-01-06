class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        val = float('inf')
        n = len(arr)
        ans = []
        for i in range(n-1):
        
            val = min(val,arr[i+1]-arr[i])
        for i in range(n-1):
            temp= []
            if arr[i+1]- arr[i] == val:
                temp.extend([arr[i],arr[i+1]])
                #ans.append([a[i],a[i+1]])
            ans.append(temp)
        return list(filter(None,ans))
            
                
        
        