func generateMatrix(n int) [][]int {
    m := make([][]int, n)
    for i := 0; i < n; i++ {
        m[i] = make([]int, n)
    }
    RecSpiral(1, 0, n-1, m)
    return m
}

func RecSpiral(current, start, end int, m [][]int) {
    if start == end {
        m[start][start] = current
        return
    }
    if start > end {
        return
    }
    for i := start; i <= end; i++ {
        m[start][i] = current
        current++
    }
    for i := start+1; i <= end; i++ {
        m[i][end] = current
        current++
    }
    for i := end-1; i >= start; i-- {
        m[end][i] = current
        current++
    }
    for i := end-1; i >= start+1; i-- {
        m[i][start] = current
        current++
    }
    RecSpiral(current, start+1, end-1, m)
}