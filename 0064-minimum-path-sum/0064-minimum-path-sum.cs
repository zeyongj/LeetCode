public class Solution {
    public int MinPathSum(int[][] grid) {
        if (grid == null || grid.Length == 0)
            return Int32.MaxValue;
        
        int[,] dp = new int[grid.Length, grid[0].Length];
        
        for (int i = 0; i < grid.Length; i++)
            for (int j = 0; j < grid[0].Length; j++)
                dp[i, j] = Int32.MaxValue;
        
        return DFS(grid, 0, 0, 0, dp);
    }
    
    private int DFS(int[][] grid, int x, int y, int cur, int[,] dp)
    {
        cur += grid[x][y];
        
         if (cur >= dp[x, y])
             return Int32.MaxValue;
        
        dp[x, y] = cur;
        
        if (x == grid.Length - 1 && y == grid[0].Length - 1)
            return cur;
        
        if (x + 1 == grid.Length)
            return DFS(grid, x, y + 1, cur, dp);
        else if (y + 1 == grid[0].Length)
            return DFS(grid, x + 1, y, cur, dp);
        else
        {
            int r = DFS(grid, x, y + 1, cur, dp),
                d = DFS(grid, x + 1, y, cur, dp);
                        
            return r <= d ? r : d;
        }
    }
}