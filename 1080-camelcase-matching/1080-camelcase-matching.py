class Solution:
    def camelMatch(self, qs, p):
        def u(s):
            return [c for c in s if c.isupper()]

        def issup(s, t):
            it = iter(t)
            return all(c in it for c in s)
        return [u(p) == u(q) and issup(p, q) for q in qs]