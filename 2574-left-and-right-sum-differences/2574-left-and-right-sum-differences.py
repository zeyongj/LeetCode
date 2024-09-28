class Solution(object):
    def rs(self,i,a):
        sum1=0
        for x in range(i+1,len(a)):
            sum1+=a[x]
        return sum1
    def ls(self,i,a):
        sum1=0
        for x in range(i):
            sum1+=a[x]
        return sum1
    def leftRightDifference(self,nums):
        answer=[]
        for i in range(len(nums)):
            answer.append(abs(self.rs(i,nums)-self.ls(i,nums)))
        return answer