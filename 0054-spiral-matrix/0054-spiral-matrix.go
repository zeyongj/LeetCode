func spiralOrder(matrix [][]int) []int {
    var res []int
    m := len(matrix)
    n := len(matrix[0])
    
    top := 0
    bottom := m - 1
    left := 0
    right := n - 1
    
    for {
        // Traverse from left to right.
        for i := left; i <= right; i++ {
            res = append(res, matrix[top][i])
        }
        top++
        if top > bottom {
            break
        }

        // Traverse from top to bottom.
        for i := top; i <= bottom; i++ {
            res = append(res, matrix[i][right])
        }
        right--
        if left > right {
            break
        }

        // Traverse from right to left.
        for i := right; i >= left; i-- {
            res = append(res, matrix[bottom][i])
        }
        bottom--
        if top > bottom {
            break
        }

        // Traverse from bottom to top.
        for i := bottom; i >= top; i-- {
            res = append(res, matrix[i][left])
        }
        left++
        if left > right {
            break
        }
    }
    
    return res
}
