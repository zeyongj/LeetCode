import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<String, Boolean> memo = new HashMap<>();

    public boolean isScramble(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        if (s1.equals(s2)) return true;
        String key = s1 + "_" + s2;
        if (memo.containsKey(key)) return memo.get(key);

        String sortedS1 = sortString(s1);
        String sortedS2 = sortString(s2);
        if (!sortedS1.equals(sortedS2)) return false;

        int n = s1.length();
        for (int i = 1; i < n; i++) {
            if ((isScramble(s1.substring(0, i), s2.substring(0, i)) && isScramble(s1.substring(i), s2.substring(i))) ||
                (isScramble(s1.substring(0, i), s2.substring(n - i)) && isScramble(s1.substring(i), s2.substring(0, n - i)))) {
                memo.put(key, true);
                return true;
            }
        }

        memo.put(key, false);
        return false;
    }

    private String sortString(String s) {
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        return new String(charArray);
    }
}
