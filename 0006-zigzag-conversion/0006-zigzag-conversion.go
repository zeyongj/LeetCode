func convert(s string, numRows int) string {
    if numRows == 1 || numRows >= len(s) {
        return s
    }
    
    res := []byte{}
    n := len(s)
    cycleLen := 2 * numRows - 2
    
    for i := 0; i < numRows; i++ {
        for j := 0; j < n; j += cycleLen {
            if j + i < n {
                res = append(res, s[j + i])
            }
            if i != 0 && i != numRows - 1 && j + cycleLen - i < n {
                res = append(res, s[j + cycleLen - i])
            }
        }
    }
    
    return string(res)
}
