class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the deck in increasing order
        deck.sort()
        
        n = len(deck)
        result = [0] * n
        indices = deque(range(n))
        
        for card in deck:
            idx = indices.popleft()  # Get the next available index
            result[idx] = card       # Place the card in the result array
            if indices:               # If there are remaining indices in the deque
                indices.append(indices.popleft())  # Move the used index to the end of deque
        
        return result