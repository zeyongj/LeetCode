class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0].isdigit(): 
            x = x[::-1]
            x = int(x)
        else: 
            x = x[1:]
            x = x[::-1]
            x = -1 * int(x)
            
        if x >= -2 ** 31 and x <= (2**31 - 1):
            return x
        else:
            return 0