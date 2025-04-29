class Solution:
    def checkOnesSegment(self, s):
        len_s = len(s)
        one_indices = []
        i = 0
        while (i < len_s):
            c = s[i]
            if (c == '1'):
                one_indices.append(i)
            i += 1
        
        len_one_indices = len(one_indices)

        i = 1
        while (i < len_one_indices):
            if (one_indices[i] - one_indices[i-1] > 1):
                return False
            i += 1

        return True