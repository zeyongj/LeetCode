class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZero, numNegOnes,k):
        output=[]
        if numOnes:
            for i in range(numOnes):
                output.append(1)
        if numZero:
            for i in range(numZero):
                output.append(0)
        if numNegOnes:
            for i in range(numNegOnes):
                output.append(-1)
        output.sort(reverse=True)
        return sum(output[:k])
       