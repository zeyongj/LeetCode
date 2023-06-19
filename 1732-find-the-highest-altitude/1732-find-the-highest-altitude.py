class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maxAltitude = 0
        length = len(gain)
        
        for i in range(0, length):
            altitude += gain[i]
            maxAltitude = max(maxAltitude, altitude)
        
        return maxAltitude

