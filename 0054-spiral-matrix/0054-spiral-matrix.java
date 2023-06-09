import java.util.*;

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<Integer>();
        int m = matrix.length;
        int n = matrix[0].length;
        
        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;
        
        while(true) {
            // Traverse from left to right.
            for (int i = left; i <= right; i++) res.add(matrix[top][i]);
            if (++top > bottom) break;

            // Traverse from top to bottom.
            for (int i = top; i <= bottom; i++) res.add(matrix[i][right]);
            if (--right < left) break;

            // Traverse from right to left.
            for (int i = right; i >= left; i--) res.add(matrix[bottom][i]);
            if (--bottom < top) break;

            // Traverse from bottom to top.
            for (int i = bottom; i >= top; i--) res.add(matrix[i][left]);
            if (++left > right) break;
        }
        
        return res;
    }
}
