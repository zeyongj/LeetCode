class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        d1_e = defaultdict(int)
        d1_o = defaultdict(int)

        d2_e = defaultdict(int)
        d2_o = defaultdict(int)
        
        for i in range(len(s1)):
            if i % 2 == 0:
                d1_e[s1[i]] += 1
                d2_e[s2[i]] += 1
            else:
                d1_o[s1[i]] += 1
                d2_o[s2[i]] += 1    
        if d1_e == d2_e and  d1_o == d2_o:
            return True
        else:
            return False        