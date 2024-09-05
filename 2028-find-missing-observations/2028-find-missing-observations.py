class Solution:
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        total_sum = mean * (n + m)
        observed_sum = sum(rolls)
        
        missing_sum = total_sum - observed_sum
        
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        base = missing_sum // n
        remainder = missing_sum % n
        
        result = [base] * n
        for i in range(remainder):
            result[i] += 1
        
        return result
