/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let res = [];
    let m = matrix.length;
    let n = matrix[0].length;
    
    let top = 0;
    let bottom = m - 1;
    let left = 0;
    let right = n - 1;
    
    while(true) {
        // Traverse from left to right.
        for (let i = left; i <= right; i++) res.push(matrix[top][i]);
        if (++top > bottom) break;

        // Traverse from top to bottom.
        for (let i = top; i <= bottom; i++) res.push(matrix[i][right]);
        if (--right < left) break;

        // Traverse from right to left.
        for (let i = right; i >= left; i--) res.push(matrix[bottom][i]);
        if (--bottom < top) break;

        // Traverse from bottom to top.
        for (let i = bottom; i >= top; i--) res.push(matrix[i][left]);
        if (++left > right) break;
    }
    
    return res;
};
