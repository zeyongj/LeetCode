class Solution {
    public boolean isPalindrome(int x) {
        String s = new StringBuilder(String.valueOf(x)).reverse().toString();
        return String.valueOf(x).equals(s);
    }
}