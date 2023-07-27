import java.util.*;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        int i = 0, n = words.length;
        while (i < n) {
            int totalChars = words[i].length();
            int j = i + 1;
            while (j < n && totalChars + 1 + words[j].length() <= maxWidth) {
                totalChars += 1 + words[j].length();
                ++j;
            }
            int spaceSlots = j - i - 1;
            int totalSpaces = maxWidth - totalChars + spaceSlots;
            
            StringBuilder line = new StringBuilder(words[i]);
            for (int k = i + 1; k < j; ++k) {
                int spaces = j == n || spaceSlots == 0 ? 1 : totalSpaces / spaceSlots + (k - i <= totalSpaces % spaceSlots ? 1 : 0);
                char[] spaceArr = new char[spaces];
                Arrays.fill(spaceArr, ' ');
                line.append(spaceArr);
                line.append(words[k]);
            }
            while (line.length() < maxWidth) {
                line.append(' ');  // append remaining spaces
            }
            res.add(line.toString());
            i = j;
        }
        return res;
    }
}
