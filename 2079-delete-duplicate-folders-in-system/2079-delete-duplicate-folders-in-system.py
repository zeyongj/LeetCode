from collections import defaultdict
from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()
        
        # Build the tree structure
        for path in paths:
            curr = root
            for name in path:
                if name not in curr.children:
                    curr.children[name] = Node()
                curr = curr.children[name]
        
        # Encode each subtree and group nodes with identical structures
        mapping = defaultdict(list)
        self._encode(root, mapping)
        
        # Mark duplicate subtrees for deletion
        for group in mapping.values():
            if len(group) > 1:
                for node in group:
                    node.deleted = True
        
        # Collect all non-deleted paths
        result = []
        self._collect(root, [], result)
        return result
    
    def _encode(self, node: Node, mapping: dict) -> str:
        if not node.children:
            return "()"
        
        parts = []
        for name, child in node.children.items():
            sub = self._encode(child, mapping)
            parts.append(name + sub)
        
        parts.sort()
        sign = "(" + "".join(parts) + ")"
        mapping[sign].append(node)
        return sign
    
    def _collect(self, node: Node, path: List[str], result: List[List[str]]):
        for name, child in node.children.items():
            if child.deleted:
                continue
            path.append(name)
            result.append(path[:])  # Create a copy of the current path
            self._collect(child, path, result)
            path.pop()
