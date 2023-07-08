func getPermutation(n int, k int) string {
    
    list := make([]string,n)
    for i := 1; i <= n; i++ {
        list[i-1] = strconv.Itoa(i)
    }
    
    factorial := make([]int,n)
    factorial[0] = 1
    for i := 1; i < n; i++ {
        factorial[i] = i * factorial[i - 1]
    }
    
    result := ""
    k = k - 1
    
    for n > 0 {
        pos := k / factorial[n - 1]
        result = result + list[pos]
        list = append(list[:pos], list[pos + 1:]...)
        k = k % factorial[n - 1]
        n = n - 1
    }
    
    return result
}