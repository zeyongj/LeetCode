class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize deque with n friends
        circle = deque(range(1, n + 1))

        # Perform eliminations while more than 1 player remains
        while len(circle) > 1:
            # Process the first k-1 friends without eliminating them
            for _ in range(k - 1):
                circle.append(circle.popleft())
            # Eliminate the k-th friend
            circle.popleft()

        return circle[0]