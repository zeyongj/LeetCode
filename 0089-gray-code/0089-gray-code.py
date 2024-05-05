class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        if n == 0:
            return [0]
       
        previous_sequence = self.grayCode(n - 1)

        add_num = 1 << (n - 1)

        result = previous_sequence + [x + add_num for x in reversed(previous_sequence)]
        return result
