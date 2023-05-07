public class Solution {
    public string CountAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        
        string previous = CountAndSay(n - 1);
        StringBuilder result = new StringBuilder();
        int count = 1;
        
        for (int i = 1; i < previous.Length; ++i) {
            if (previous[i] == previous[i - 1]) {
                count++;
            } else {
                result.Append(count).Append(previous[i - 1]);
                count = 1;
            }
        }
        
        result.Append(count).Append(previous[previous.Length - 1]);
        
        return result.ToString();
    }
}
