class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        d = defaultdict(list)

        for i, ch in enumerate(s):
            d[ch].append(i)

        return all(b-a-1 == distance[ord(ch)-97] for ch, (a,b) in d.items())