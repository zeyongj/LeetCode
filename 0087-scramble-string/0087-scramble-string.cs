using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<string, bool> memo = new Dictionary<string, bool>();

    public bool IsScramble(string s1, string s2) {
        if (s1.Length != s2.Length) return false;
        if (s1 == s2) return true;
        string key = s1 + "_" + s2;
        if (memo.ContainsKey(key)) return memo[key];

        string sortedS1 = SortString(s1);
        string sortedS2 = SortString(s2);
        if (sortedS1 != sortedS2) return false;

        int n = s1.Length;
        for (int i = 1; i < n; i++) {
            if ((IsScramble(s1.Substring(0, i), s2.Substring(0, i)) && IsScramble(s1.Substring(i), s2.Substring(i))) ||
                (IsScramble(s1.Substring(0, i), s2.Substring(n - i)) && IsScramble(s1.Substring(i), s2.Substring(0, n - i)))) {
                memo[key] = true;
                return true;
            }
        }

        memo[key] = false;
        return false;
    }

    private string SortString(string s) {
        char[] charArray = s.ToCharArray();
        Array.Sort(charArray);
        return new string(charArray);
    }
}
