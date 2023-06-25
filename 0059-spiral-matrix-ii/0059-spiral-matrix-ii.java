public class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int num = 1;

        while (true) {
            for (int i = left; i <= right; i++) matrix[top][i] = num++; // Fill the top row
            if (++top > bottom) break;

            for (int i = top; i <= bottom; i++) matrix[i][right] = num++; // Fill the right column
            if (--right < left) break;

            for (int i = right; i >= left; i--) matrix[bottom][i] = num++; // Fill the bottom row
            if (--bottom < top) break;

            for (int i = bottom; i >= top; i--) matrix[i][left] = num++; // Fill the left column
            if (++left > right) break;
        }
        return matrix;
    }
}
