impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        if m == 0 || n == 0 {
            return 0;
        }

        let m: usize = m as usize;
        let n: usize = n as usize;
        
        let mut path: Vec<Vec<i32>> = vec![vec![0; n]; m];        
        for i in 0..m {
            for j in 0..n {
                if i == 0 || j == 0 {
                    path[i][j] = 1;
                } else {
                    path[i][j] = path[i - 1][j] + path[i][j - 1];
                }
            }
        }
        path[m - 1][n - 1]
    }
}