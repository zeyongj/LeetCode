class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        generate("", n, 0, 0, result);
        return result;
    }
    
    private void generate(String current, int n, int open, int close, List<String> result) {
        if (open == n && close == n) {
            result.add(current);
            return;
        }
        
        if (open < n) {
            generate(current + "(", n, open+1, close, result);
        }
        
        if (close < open) {
            generate(current + ")", n, open, close+1, result);
        }
    }
}
