class Solution:
    
    def combineTwo(self, a, b):
        if b in a:
            return a
        i = 0
        while i < len(a):
            ch = a[i:]
            pos = b.find(ch)
            if pos == 0:
                j = len(ch)
                return a + b[j:]
            i += 1
        return a + b
    
    def minRes(self, res, abc):
        if res == "":
            return abc
        if len(res) > len(abc):
            return abc
        if len(res) == len(abc) and res > abc:
            return abc
        return res
    
    def minimumString(self, a, b, c):
        v = [a, b, c]
        res = ""
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k and k != i:
                        ab = self.combineTwo(v[i], v[j])
                        abc = self.combineTwo(ab, v[k])
                        res = self.minRes(res, abc)
                        if i == 2 and j == 0 and k == 1:
                            print(ab, abc)
        return res