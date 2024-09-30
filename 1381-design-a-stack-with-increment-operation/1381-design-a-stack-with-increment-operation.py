class CustomStack:

    def __init__(self, n: int):
        self.n, self.stack, self.inc = n, [], []

    def push(self, x: int) -> None:
        if len(self.stack) < self.n: self.stack.append(x), self.inc.append(0)

    def pop(self) -> int:
        if not self.stack: return -1
        if len(self.inc) > 1: self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc: self.inc[min(k, len(self.inc)) - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)