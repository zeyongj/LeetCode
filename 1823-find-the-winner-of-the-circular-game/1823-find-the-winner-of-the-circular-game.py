class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # Josephus problem is 0-indexed in calculation
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1