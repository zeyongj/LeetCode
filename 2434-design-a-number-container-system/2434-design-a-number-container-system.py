import heapq
class NumberContainers:
    def __init__(self):
        self.m = {}
        self.d = {}
    def change(self, i, n):
        if i in self.m and self.m[i]==n: return
        self.m[i] = n
        self.d.setdefault(n, [])
        heapq.heappush(self.d[n], i)
    def find(self, n):
        if n not in self.d: return -1
        while self.d[n] and self.m.get(self.d[n][0])!=n:
            heapq.heappop(self.d[n])
        return self.d[n][0] if self.d[n] else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)