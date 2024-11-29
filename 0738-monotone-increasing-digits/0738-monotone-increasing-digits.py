class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
		# max size of string
        self.maxlen = len(str(n))
		# maximum ans store here
        self.maxans = 0
        self.find(str(n))
        return self.maxans
    
    def find(self,num,idx=0,curnum='',pb=None):
        if idx == self.maxlen:
            self.maxans = max(self.maxans,int(curnum))
        if idx >= self.maxlen or self.maxans:
            return
        if not pb:
            for i in range(int(num[idx]),-1,-1):
                self.find(num,idx+1,curnum+str(i),num[idx])
        else:
            for i in range(9,int(pb)-1,-1):
                if int(curnum+str(i))<=int(num[:idx+1]):
                    self.find(num,idx+1,curnum+str(i),num[idx])