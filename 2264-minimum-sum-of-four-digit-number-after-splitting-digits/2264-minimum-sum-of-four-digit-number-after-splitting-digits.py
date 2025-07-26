class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num),reverse=True)
        n = len(num)    
        res = 0
        even_iteration = False
        position = 0
        for i in range(n):
            res += int(num[i])*(10**position)
            if even_iteration:
                position += 1
                even_iteration = False
            else:
                even_iteration = True
        return res