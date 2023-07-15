class Solution:
    def isNumber(self, s: str) -> bool:
        state = 0
        finals = {2, 3, 7, 8}
        transfer = {
            (0, 'blank'): 0, (0, 'sign'): 1, (0, 'digit'): 2, (0, '.'): 4,
            (1, 'digit'): 2, (1, '.'): 4,
            (2, 'digit'): 2, (2, '.'): 3, (2, 'e'): 5, (2, 'blank'): 8,
            (3, 'digit'): 3, (3, 'e'): 5, (3, 'blank'): 8,
            (4, 'digit'): 3,
            (5, 'sign'): 6, (5, 'digit'): 7,
            (6, 'digit'): 7,
            (7, 'digit'): 7, (7, 'blank'): 8,
            (8, 'blank'): 8
        }

        for c in s:
            if '0' <= c <= '9':
                t = 'digit'
            elif c in "+-":
                t = 'sign'
            elif c in "eE":
                t = 'e'
            elif c in ". ":
                t = c
            else:
                t = 'invalid'
            
            if (state, t) not in transfer:
                return False
            state = transfer[(state, t)]
        
        return state in finals
