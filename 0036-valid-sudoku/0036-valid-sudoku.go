func isValidSudoku(board [][]byte) bool {
    seen := make(map[string]bool)
    
    for i := 0; i < 9; i++ {
        for j := 0; j < 9; j++ {
            number := board[i][j]
            if number != '.' {
                row := string(number) + " seen in row " + string(i)
                col := string(number) + " seen in col " + string(j)
                box := string(number) + " seen in box " + string(i/3) + "-" + string(j/3)
                
                if seen[row] || seen[col] || seen[box] {
                    return false
                }
                
                seen[row] = true
                seen[col] = true
                seen[box] = true
            }
        }
    }
    
    return true
}
