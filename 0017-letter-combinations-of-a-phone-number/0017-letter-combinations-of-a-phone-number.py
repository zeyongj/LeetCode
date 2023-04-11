from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        self.backtrack('', digits, 0, phone, result)
        return result
    
    def backtrack(self, combination: str, digits: str, index: int, phone: dict, result: List[str]) -> None:
        if index == len(digits):
            result.append(combination)
            return
        
        letters = phone[digits[index]]
        for letter in letters:
            self.backtrack(combination + letter, digits, index + 1, phone, result)
