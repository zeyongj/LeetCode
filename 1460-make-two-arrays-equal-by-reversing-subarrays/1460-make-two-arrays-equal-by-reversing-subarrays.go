func canBeEqual(targetArray []int, currentArray []int) bool {
    elementCounts := make([]int, 1001)
    uniqueCount := 0
    
    for i := 0; i < len(targetArray); i++ {
        if elementCounts[targetArray[i]] == 0 {
            uniqueCount++
        }
        elementCounts[targetArray[i]]++
        
        if elementCounts[currentArray[i]] == 1 {
            uniqueCount--
        }
        elementCounts[currentArray[i]]--
    }
    
    return uniqueCount == 0
}