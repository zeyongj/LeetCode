class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:

        ctr = Counter(map(tuple,pick))

        return len({player for (player,_), count in ctr.items() if count > player})