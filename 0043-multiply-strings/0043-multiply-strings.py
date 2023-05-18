class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                temp_sum = result[i + j + 1] + product
                result[i + j + 1] = temp_sum % 10
                result[i + j] += temp_sum // 10
        
        # Remove leading zeros
        while result[0] == 0:
            result.pop(0)
        
        return ''.join(map(str, result))
