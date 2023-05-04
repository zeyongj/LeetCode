using System;
using System.Collections.Generic;

public class Solution {
    public bool IsValidSudoku(char[][] board) {
        HashSet<string> seen = new HashSet<string>();
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char number = board[i][j];
                if (number != '.') {
                    string row = number + " seen in row " + i;
                    string col = number + " seen in col " + j;
                    string box = number + " seen in box " + i / 3 + "-" + j / 3;
                    
                    if (seen.Contains(row) || seen.Contains(col) || seen.Contains(box)) {
                        return false;
                    }
                    
                    seen.Add(row);
                    seen.Add(col);
                    seen.Add(box);
                }
            }
        }
        
        return true;
    }
}
