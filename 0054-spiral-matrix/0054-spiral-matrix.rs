impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        if matrix.is_empty() || matrix[0].is_empty() {
            return vec![];
        }
        
        let (mut top, mut bottom, mut left, mut right) = (0, matrix.len() - 1, 0, matrix[0].len() - 1);
        let mut res = Vec::with_capacity((bottom + 1) * (right + 1));

        loop {
            // Traverse from left to right.
            for i in left..=right {
                res.push(matrix[top][i]);
            }
            top += 1;
            if top > bottom {
                break;
            }

            // Traverse from top to bottom.
            for i in top..=bottom {
                res.push(matrix[i][right]);
            }
            if right == 0 || left == right {
                break;
            }
            right -= 1;

            // Traverse from right to left.
            for i in (left..=right).rev() {
                res.push(matrix[bottom][i]);
            }
            if bottom == 0 || top == bottom {
                break;
            }
            bottom -= 1;

            // Traverse from bottom to top.
            for i in (top..=bottom).rev() {
                res.push(matrix[i][left]);
            }
            left += 1;
            if left > right {
                break;
            }
        }
        res
    }
}
