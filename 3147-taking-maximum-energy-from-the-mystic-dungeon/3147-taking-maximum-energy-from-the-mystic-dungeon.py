class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res, n = -math.inf, len(energy)

        # iterate through every possible starting position
        for p in range(k):
            acc_energy = 0
            
            # iterate from the right to left, in k-steps
            for i in range(n-p-1, -1, -k):
                acc_energy += energy[i]
                res = max(res, acc_energy)

        return res