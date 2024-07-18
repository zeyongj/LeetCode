class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = 2 * n
        n3 = 3 * n
        
        nums = str(n) + str(n2) + str(n3)
        
        num_dic = {}
        
        for num in nums:
            if num not in num_dic:
                if num == '0':
                    return False
                else:
                    num_dic[num] = 1
            else:
                return False
        
        return True