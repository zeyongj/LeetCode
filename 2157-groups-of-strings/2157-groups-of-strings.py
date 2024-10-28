class Solution:
    def groupStrings(self, words):
        n = len(words)
        m = {}
        f = []
        
        def find(x):
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        
        def connected(x):
            for i in range(26):
                yield x ^ (1 << i)
                if (x & (1 << i)) > 0:
                    for j in range(26):
                         if x & (1 << j) == 0:
                            yield x ^ (1 << i) ^ (1 << j)

        for i,w in enumerate(words):
            x = sum(1 << (ord(c) - ord('a')) for c in w)
            f.append(m.setdefault(x, i))
            for y in connected(x):
                if y in m:
                    i, j = find(m[x]), find(m[y])
                    if i != j:
                        f[i] = j

        count = collections.Counter(find(i) for i in range(n))
        return [len(count), max(count.values())]