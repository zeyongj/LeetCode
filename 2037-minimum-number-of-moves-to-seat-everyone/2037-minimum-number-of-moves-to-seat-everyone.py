class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = 0
        seats.sort()
        students.sort()
        studentSize = len(students)
        for s in range(studentSize):
            moves += abs(students[s]-seats[s])
        return moves