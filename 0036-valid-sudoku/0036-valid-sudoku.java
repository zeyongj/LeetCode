import java.util.HashSet;
import java.util.Set;

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> seen = new HashSet<>();
        
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char number = board[i][j];
                if (number != '.') {
                    String row = number + " seen in row " + i;
                    String col = number + " seen in col " + j;
                    String box = number + " seen in box " + i / 3 + "-" + j / 3;
                    
                    if (seen.contains(row) || seen.contains(col) || seen.contains(box)) {
                        return false;
                    }
                    
                    seen.add(row);
                    seen.add(col);
                    seen.add(box);
                }
            }
        }
        
        return true;
    }
}
