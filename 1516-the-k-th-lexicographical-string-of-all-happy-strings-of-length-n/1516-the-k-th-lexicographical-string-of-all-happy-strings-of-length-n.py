class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def generate(prev):
            if len(prev) == n:
                yield prev
                return
            for c in 'abc':
                if not prev or c != prev[-1]:
                    yield from generate(prev + c)
            
        for i, res in enumerate(generate(''), 1):            
            if i == k:
                return res
        return ''  