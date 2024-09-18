class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = [i for i in range(26)]
    
        def get(x):
            # recursively get the root element
            if x == root[x]:
                return x 
            else:
                return get(root[x])
        
        # unite two elements
        def unite(x, y):
            # find the root of x and y, 
            x = get(x)
            y = get(y)
            # if their roots are not same, we combine them
            if x != y:
                if x < y:
                    root[y] = x
                else:
                    root[x] = y
            return
        
        ans = ""
        for i in range(len(s1)):
            unite(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        # dsu to build the final answer from the root element (smallest)
        for x in baseStr:
            ans += chr(get(ord(x) - ord('a')) + ord('a'))
        return ans