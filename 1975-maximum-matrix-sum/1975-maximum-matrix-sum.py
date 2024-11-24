class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_value = float('inf')  # Equivalent to Integer.MAX_VALUE
        total_sum = 0
        neg_count = 0

        for row in matrix:
            for value in row:
                if value < 0:
                    neg_count += 1
                abs_value = abs(value)
                min_value = min(min_value, abs_value)
                total_sum += abs_value

        if neg_count % 2 == 0:
            return total_sum
        return total_sum - 2 * min_value        