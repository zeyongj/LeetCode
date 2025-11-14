class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashmap: dict[float, int] = defaultdict(int)
        for w, h in rectangles:
            hashmap[w / h] += 1
        output: int = 0
        for ratio, freq in hashmap.items():
            output += freq * (freq - 1) // 2
        return output