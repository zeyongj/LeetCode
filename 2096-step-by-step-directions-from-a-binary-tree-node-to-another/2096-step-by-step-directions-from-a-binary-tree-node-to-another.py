# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self, root: TreeNode, startValue: int, destValue: int
    ) -> str:
        # Map to store parent nodes
        parent_map = {}

        # Find the start node and populate parent map
        start_node = self._find_start_node(root, startValue)
        self._populate_parent_map(root, parent_map)

        # Perform BFS to find the path
        q = deque([start_node])
        visited_nodes = set()
        # Key: next node, Value: <current node, direction>
        path_tracker = {}
        visited_nodes.add(start_node)

        while q:
            current_element = q.popleft()

            # If destination is reached, return the path
            if current_element.val == destValue:
                return self._backtrack_path(current_element, path_tracker)

            # Check and add parent node
            if current_element.val in parent_map:
                parent_node = parent_map[current_element.val]
                if parent_node not in visited_nodes:
                    q.append(parent_node)
                    path_tracker[parent_node] = (current_element, "U")
                    visited_nodes.add(parent_node)

            # Check and add left child
            if (
                current_element.left
                and current_element.left not in visited_nodes
            ):
                q.append(current_element.left)
                path_tracker[current_element.left] = (current_element, "L")
                visited_nodes.add(current_element.left)

            # Check and add right child
            if (
                current_element.right
                and current_element.right not in visited_nodes
            ):
                q.append(current_element.right)
                path_tracker[current_element.right] = (current_element, "R")
                visited_nodes.add(current_element.right)

        # This line should never be reached if the tree is valid
        return ""

    def _backtrack_path(self, node, path_tracker):
        path = []
        # Construct the path
        while node in path_tracker:
            # Add the directions in reverse order and move on to the previous node
            path.append(path_tracker[node][1])
            node = path_tracker[node][0]
        path.reverse()
        return "".join(path)

    def _populate_parent_map(self, node, parent_map):
        if not node:
            return

        # Add children to the map and recurse further
        if node.left:
            parent_map[node.left.val] = node
            self._populate_parent_map(node.left, parent_map)

        if node.right:
            parent_map[node.right.val] = node
            self._populate_parent_map(node.right, parent_map)

    def _find_start_node(self, node, start_value):
        if not node:
            return None

        if node.val == start_value:
            return node

        left_result = self._find_start_node(node.left, start_value)

        # If left subtree returns a node, it must be StartNode. Return it
        # Otherwise, return whatever is returned by right subtree.
        if left_result:
            return left_result
        return self._find_start_node(node.right, start_value)