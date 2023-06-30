impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (obstacle_grid.len(), obstacle_grid[0].len());
        if obstacle_grid[0][0] == 1 || obstacle_grid[m - 1][n - 1] == 1 {
            return 0;
        }

        let mut dp = vec![vec![0; n]; m];
        dp[0][0] = 1;

        obstacle_grid.iter().enumerate().for_each(|(i, row)| {
            row.iter()
                .enumerate()
                .filter(|(_, x)| **x == 0)
                .for_each(|(j, _)| {
                    if i > 0 {
                        dp[i][j] += dp[i - 1][j];
                    }
                    if j > 0 {
                        dp[i][j] += dp[i][j - 1];
                    }
                })
        });

        dp[m - 1][n - 1]
    }
}