class Solution:
    def smallestDistancePair(self, numbers: List[int], k: int) -> int:
        numbers.sort()
        minDistance, maxDistance = 0, numbers[-1] - numbers[0]
        
        while minDistance < maxDistance:
            midDistance = (minDistance + maxDistance) // 2
            if self.countPairsWithinDistance(numbers, midDistance) < k:
                minDistance = midDistance + 1
            else:
                maxDistance = midDistance
        
        return minDistance

    def countPairsWithinDistance(self, numbers: List[int], targetDistance: int) -> int:
        count = left = 0
        for right in range(1, len(numbers)):
            while numbers[right] - numbers[left] > targetDistance:
                left += 1
            count += right - left
        return count