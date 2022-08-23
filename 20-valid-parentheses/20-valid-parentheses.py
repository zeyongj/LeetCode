class Solution:
    def isValid(self, s: str) -> bool:
        mapClose2Open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        ans = []
        for element in s:
            condition = (element == '(' or element == '[' or element == '{')
            if condition:
                ans.append(element)
            else:
                if len(ans) == 0 or ans[-1] != mapClose2Open[element]: 
                    return False
                ans.pop()
        return len(ans) == 0