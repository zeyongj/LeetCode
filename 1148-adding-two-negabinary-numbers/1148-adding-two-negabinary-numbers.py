class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lookup = {
            -2: (0, 1), # useless becos −2 occurs only during subtraction
            -1: (1, 1),
            0: (0, 0),
            1: (1, 0),
            2: (0, -1),
            3: (1, -1),
        }
        carry = 0
        result = []
        # do addition
        while len(arr1) > 0 or len(arr2) > 0:
            a = 0
            if len(arr1) > 0:
                a = arr1.pop()
            b = 0
            if len(arr2) > 0:
                b = arr2.pop()
            temp = a + b + carry
            res, carry = lookup[temp]
            result.append(res)
        # if there is still a carry
        while carry != 0:
            res, carry = lookup[carry]
            result.append(res)
        # remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]        