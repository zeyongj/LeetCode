class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        // If there is only one word to check, this is a trivial case with
        // not enough input (minimum two words) to run the algorithm.
        // So we return True
        if (words.length == 1)
            return true;

        // Declare a hash map to store the characters of the words
        Map<Character, Integer> orderMap = new HashMap<>();

        // Traverse order and store the rank of each letter in orderMap
        for (int i = 0; i < order.length(); i++) {
            orderMap.put(order.charAt(i), i);
        }

        for (int i = 0; i < words.length - 1; i++) {
            // Traverse each character in a word
            for (int j = 0; j < words[i].length(); j++) {
                // If all the letters have matched so far, but the current word
                // is longer than the next one, the two are not in order and
                // we return False
                if (j >= words[i + 1].length())
                    return false;

                // Check if the letters in the same position in the two words
                // are different
                if (words[i].charAt(j) != words[i + 1].charAt(j)) {
                    // Check if the rank of the letter in the current word is
                    // greater than the rank in the same position in the next word
                    if (orderMap.get(words[i].charAt(j)) > orderMap.get(words[i + 1].charAt(j))) {
                        return false;
                    } else {
                        // if we find the first different character and they are sorted,
                        // then there's no need to check remaining letters
                        break;
                    }
                }
            }
        }

        return true;
    }
}