class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        profit = 0
        mn = float('inf')
        totalEnergy = currentEnergy
        
        for energy in enemyEnergies:
            if energy < mn:
                mn = energy
            totalEnergy += energy
        
        if currentEnergy < mn:
            return 0
        
        totalEnergy -= mn
        return totalEnergy // mn