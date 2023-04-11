using System;
using System.Collections.Generic;

public class Solution {
    private void Backtrack(string combination, string digits, int index, string[] phone, IList<string> result) {
        if (index == digits.Length) {
            result.Add(combination);
            return;
        }

        string letters = phone[digits[index] - '0'];
        for (int i = 0; i < letters.Length; i++) {
            Backtrack(combination + letters[i], digits, index + 1, phone, result);
        }
    }

    public IList<string> LetterCombinations(string digits) {
        if (string.IsNullOrEmpty(digits)) {
            return new List<string>();
        }

        string[] phone = {
            "0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        };

        List<string> result = new List<string>();
        Backtrack("", digits, 0, phone, result);
        return result;
    }
}
