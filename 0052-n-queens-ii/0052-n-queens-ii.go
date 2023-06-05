func totalNQueens(n int) int {
    cols := make([]bool, n)
    hillDiagonals := make([]bool, 2*n)
    daleDiagonals := make([]bool, 2*n)
    return backtrack(0, n, cols, hillDiagonals, daleDiagonals)
}

func backtrack(row, n int, cols, hills, dales []bool) int {
    count := 0
    for i := 0; i < n; i++ {
        if !cols[i] && !hills[row-i+n] && !dales[row+i] {
            cols[i] = true
            hills[row-i+n] = true
            dales[row+i] = true

            if row == n-1 {
                count++
            } else {
                count += backtrack(row+1, n, cols, hills, dales)
            }

            cols[i] = false
            hills[row-i+n] = false
            dales[row+i] = false
        }
    }
    return count
}
