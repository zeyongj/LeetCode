class Solution {
    public int lengthOfLastWord(String s) {
        int length = 0;
        int pos = s.length() - 1;

        // Skip trailing spaces if any
        while (pos >= 0 && s.charAt(pos) == ' ') {
            --pos;
        }

        // Count characters in the last word
        while (pos >= 0 && s.charAt(pos) != ' ') {
            --pos;
            ++length;
        }

        return length;       
    }
}