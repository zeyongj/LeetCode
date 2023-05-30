impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        
        // Transpose the matrix
        for i in 0..n {
            for j in i..n {
                let temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        // Reverse each row
        for row in matrix.iter_mut() {
            let mid = n / 2;
            for j in 0..mid {
                let temp = row[j];
                row[j] = row[n - j - 1];
                row[n - j - 1] = temp;
            }
        }
    }
}
