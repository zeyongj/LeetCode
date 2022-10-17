class Solution {
    public boolean checkIfPangram(String sentence) {
        Set<Character> seen = new HashSet<>();
        
        for (char currChar: sentence.toCharArray())
            seen.add(currChar);
        
        if (seen.size() == 26)
            return true;
        else
            return false;
    }
}