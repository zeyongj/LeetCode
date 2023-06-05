/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    let count = 0;

    const DFS = (queens, xyDiff, xySum) => {
        let p = queens.length;
        if (p == n) {
            count++;
            return;
        }
        for (let q = 0; q < n; q++) {
            if (!queens.includes(q) && !xyDiff.includes(p-q) && !xySum.includes(p+q)) {
                DFS(queens.concat(q), xyDiff.concat(p-q), xySum.concat(p+q));
            }
        }
    }

    DFS([], [], []);
    return count;
};
