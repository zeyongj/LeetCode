using System.Collections.Generic;

public class Solution {
    public IList<int> SpiralOrder(int[][] matrix) {
        List<int> res = new List<int>();
        int m = matrix.Length;
        int n = matrix[0].Length;
        
        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;
        
        while(true) {
            // Traverse from left to right.
            for (int i = left; i <= right; i++) res.Add(matrix[top][i]);
            if (++top > bottom) break;

            // Traverse from top to bottom.
            for (int i = top; i <= bottom; i++) res.Add(matrix[i][right]);
            if (--right < left) break;

            // Traverse from right to left.
            for (int i = right; i >= left; i--) res.Add(matrix[bottom][i]);
            if (--bottom < top) break;

            // Traverse from bottom to top.
            for (int i = bottom; i >= top; i--) res.Add(matrix[i][left]);
            if (++left > right) break;
        }
        
        return res;
    }
}
