class Solution {
    public boolean isValid(String s) {
                Stack<Character> stack = new Stack<>();
        for(Character ch : s.toCharArray()){
            boolean condition = ch.equals('(') || ch.equals('[') || ch.equals('{');
            if(condition){
                stack.push(ch);
            } else if(ch.equals(')')){
                if(stack.empty()) return false;
                else if(!stack.peek().equals('(')) return false;
                else stack.pop();
            } else if(ch.equals(']')){
                if(stack.empty()) return false;
                else if(!stack.peek().equals('[')) return false;
                else stack.pop();
            } else if(ch.equals('}')){
                if(stack.empty()) return false;
                else if(!stack.peek().equals('{')) return false;
                else stack.pop();
            } else {
                throw new IllegalArgumentException("Incorrect Character: '" + ch + "'");
            }
        }
        
        return stack.empty();
    }
}