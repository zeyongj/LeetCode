class LockingTree:

    def __init__(self, parent: List[int]):
        self.locks = [0 for _ in range(len(parent))]
        self.parent = parent
        self.children = collections.defaultdict(list)
        for c, p in enumerate(parent): self.children[p].append(c)
        

    def lock(self, num: int, user: int) -> bool:
        if self._is_locked(num): return False
        self.locks[num] = user
        return True


    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] != user: return False
        self.locks[num] = 0
        return True


    def upgrade(self, num: int, user: int) -> bool:
        if self._is_locked(num): return False
        if not self._have_locked_descendant(num): return False
        if self._have_locked_ancestor(num): return False
        self.lock(num, user)
        stack = [num for num in self.children[num]]
        while stack:
            node = stack.pop()
            self.locks[node] = 0
            stack.extend(self.children[node])

        return True


    def _is_locked(self, num: int) -> bool:
        return self.locks[num] != 0


    def _have_locked_descendant(self, num: int) -> bool:
        stack = [num for num in self.children[num]]
        while stack:
            node = stack.pop()
            if self._is_locked(node): return True
            stack.extend(self.children[node])
        return False


    def _have_locked_ancestor(self, num: int) -> bool:
        while self.parent[num] != -1:
            if self._is_locked(self.parent[num]): return True
            num = self.parent[num]
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)