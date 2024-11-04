class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        res= [1]*n
        if 1 not in set(nums):
            return res
        seen = set([])
        graph = {i:set([]) for i in range(n)}
        for i,p in enumerate(parents):
            if p >= 0:
                graph[p].add(i)
        def dfs(node):
            seen.add(nums[node])
            for child in graph[node]:
                if nums[child] not in seen:
                    seen.add(nums[child])
                    dfs(child)
        
        i = nums.index(1)
        t = 1
        while i!=-1:
            dfs(i)
            while t in seen:
                t += 1
            res[i] = t
            i = parents[i]
        return res