import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) return new ArrayList<>();
        
        Map<Character, String> phone = new HashMap<Character, String>() {{
            put('2', "abc");
            put('3', "def");
            put('4', "ghi");
            put('5', "jkl");
            put('6', "mno");
            put('7', "pqrs");
            put('8', "tuv");
            put('9', "wxyz");
        }};
        
        List<String> result = new ArrayList<>();
        backtrack("", digits, 0, phone, result);
        return result;
    }
    
    private void backtrack(String combination, String digits, int index, Map<Character, String> phone, List<String> result) {
        if (index == digits.length()) {
            result.add(combination);
            return;
        }
        
        String letters = phone.get(digits.charAt(index));
        for (char letter : letters.toCharArray()) {
            backtrack(combination + letter, digits, index + 1, phone, result);
        }
    }
}
