class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        ts = 60 * int(startTime[:2]) + int(startTime[-2:])
        tf = 60 * int(finishTime[:2]) + int(finishTime[-2:])
        if 0 <= tf - ts < 15: return 0 # edge case 
        return tf//15 - (ts+14)//15 + (ts>tf)*96