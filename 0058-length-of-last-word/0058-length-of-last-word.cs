public class Solution {
    public int LengthOfLastWord(string s) {
        int length = 0;
        int pos = s.Length - 1;

        // Skip trailing spaces if any
        while (pos >= 0 && s[pos] == ' ') {
            --pos;
        }

        // Count characters in the last word
        while (pos >= 0 && s[pos] != ' ') {
            --pos;
            ++length;
        }

        return length;           
    }
}