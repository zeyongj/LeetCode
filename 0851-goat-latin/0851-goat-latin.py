class Solution(object):
    def toGoatLatin(self, sentence):
        vowels='AEIOUaeiou'
        l=sentence.split()
        l2=[]
        for i in range(len(l)):
            if l[i][0] in vowels:
                a=l[i]+'ma'+('a'*(i+1))
                l2.append(a)
            else:
                x=l[i][:1]
                b=l[i][1:]+x+'ma'+('a'*(i+1))
                l2.append(b)
        return ' '.join(l2)    
        
        