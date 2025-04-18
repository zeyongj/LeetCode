class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:

                                                    # Ex: aliceValues = [9,8,3,8], bobValues = [10,6,9,5]
        arr = sorted(zip(aliceValues, bobValues), 
                     key = lambda x: -sum(x))       #     arr = [(9,10), (8,6), (8,5), (3,9)]
        
        a = sum([i[0] for i in arr[0::2]])          #     a = sum(9 + 8) = 17
        b = sum([i[1] for i in arr[1::2]])          #     b = sum(6 + 9) = 15
        
        return (a>=b) - (a<=b)                      #     return (a>=b) - (a<=b) = (17>=15) - (1<=17) 
													#                            = 1-0 = 1