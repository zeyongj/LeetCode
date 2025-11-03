class Solution:
    def circularGameLosers(self, n, k):

        remain, ball, nxt = set(N:=range(1,n)), k,0

        for _ in N:                         

            nxt = (nxt + ball)%n            #  ball     nxt    remain
            if nxt not in remain: break     #  -----   -----   -----
                                            #    2       0     [1, 2, 3, 4]
            remain.remove(nxt)              #    4       2     [1, 3, 4]
            ball+= k                        #    6       1     [3, 4]
                                            #    6       2     [3, 4] <-- 2 appears again

        return [i+1 for i in remain]        