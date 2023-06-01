using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        if (strs.Length == 0) return new List<IList<string>>();
        
        Dictionary<string, List<string>> ans = new Dictionary<string, List<string>>();
        foreach (string s in strs) {
            char[] ca = s.ToCharArray();
            Array.Sort(ca);
            string key = new string(ca);
            
            if (!ans.ContainsKey(key)) {
                ans[key] = new List<string>();
            }
            
            ans[key].Add(s);
        }
        
        return ans.Values.ToList<IList<string>>();
    }
}
