class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_surplus = 0
        current_surplus = 0
        start_station = 0
    
        for i in range(len(gas)):
            current_surplus += gas[i] - cost[i]

            if current_surplus < 0:
                start_station = i + 1
                current_surplus = 0

            total_surplus += gas[i] - cost[i]

        if total_surplus >= 0:
            return start_station
        else:
            return -1