class Solution:
    def secondGreaterElement(self, A: List[int]) -> List[int]:
        res, s1, s2 = [-1] * len(A), [], []
        for i,a in enumerate(A):
            while s2 and A[s2[-1]] < a:
                res[s2.pop()] = a;
            tmp = []
            while s1 and A[s1[-1]] < a:
                tmp.append(s1.pop())
            s2 += tmp[::-1]
            s1.append(i)
        return res