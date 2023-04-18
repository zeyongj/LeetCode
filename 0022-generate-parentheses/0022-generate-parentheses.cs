using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        List<string> result = new List<string>();
        GenerateParenthesisHelper(result, "", 0, 0, n);
        return result;
    }

    private void GenerateParenthesisHelper(List<string> result, string current, int open, int close, int n) {
        if (current.Length == n * 2) {
            result.Add(current);
            return;
        }

        if (open < n) {
            GenerateParenthesisHelper(result, current + "(", open + 1, close, n);
        }
        
        if (close < open) {
            GenerateParenthesisHelper(result, current + ")", open, close + 1, n);
        }
    }
}
