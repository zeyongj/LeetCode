class Solution:
    def makeSimilar(self, N: List[int], T: List[int]) -> int:
            N.sort(key=lambda x: [x % 2, x])
            T.sort(key=lambda x: [x % 2, x])
            
            return sum(abs(n - t) for n, t in zip(N, T)) // 4