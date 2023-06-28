/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const res = [];
    for (let i = 0; i < n; i++) res.push([...new Array(m).fill(1)]); // initialize list
    for (let i = 1; i < n; i++) {
        for (let j = 1; j < m; j++) {
            res[i][j] = res[i-1][j] + res[i][j-1];
        }
    }
    return res[n-1][m-1];
};