class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        
        stack = []
        
        for component in components:
            if component == "" or component == ".":
                continue # Current Directory
            elif component == "..":
                size = len(stack)
                if size != 0:
                    stack.pop() # Move up one directory
            else:
                stack.append(component)
        
        return "/" + "/".join(stack)