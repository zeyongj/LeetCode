impl Solution {
    pub fn total_n_queens(n: i32) -> i32 {
        let mut count = 0;
        let mut queens = vec![-1; n as usize];
        Solution::backtrack(0, &mut queens, &mut count);
        count
    }
    
    fn backtrack(row: usize, queens: &mut Vec<i32>, count: &mut i32) {
        let n = queens.len();
        if row == n {
            *count += 1;
            return;
        }
        
        for col in 0..n {
            if Solution::is_valid(row, col, queens) {
                queens[row] = col as i32;
                Solution::backtrack(row + 1, queens, count);
                queens[row] = -1;
            }
        }
    }
    
    fn is_valid(row: usize, col: usize, queens: &Vec<i32>) -> bool {
        for r in 0..row {
            if queens[r] == col as i32 || (row - r) as i32 == (col as i32 - queens[r]).abs() {
                return false;
            }
        }
        true
    }
}
