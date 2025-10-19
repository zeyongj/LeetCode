class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxRight = -1  # Initialize the maximum element on the right as -1

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            # Store the current element before it gets overwritten
            current = arr[i]
            # Replace the current element with the max element to its right
            arr[i] = maxRight
            # Update the maxRight with the maximum of current and maxRight
            maxRight = max(maxRight, current)
        
        return arr