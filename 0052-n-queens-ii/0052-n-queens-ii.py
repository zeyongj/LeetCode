class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_place(pos, ocuppied_positions):
            for i in range(len(ocuppied_positions)):
                if ocuppied_positions[i] == pos or \
                    ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                    ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                    return False
            return True

        def place_queens(n, index, ocuppied_positions, answer):
            if index == n:
                answer[0] += 1
                return
            for i in range(n):
                if can_place(i, ocuppied_positions):
                    ocuppied_positions.append(i)
                    place_queens(n, index + 1, ocuppied_positions, answer)
                    ocuppied_positions.pop()

        answer = [0]
        place_queens(n, 0, [], answer)
        return answer[0]
