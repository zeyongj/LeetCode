import (
    "strings"
)

func multiply(num1 string, num2 string) string {
    if num1 == "0" || num2 == "0" {
        return "0"
    }
    
    len1 := len(num1)
    len2 := len(num2)
    result := make([]int, len1 + len2)
    
    for i := len1 - 1; i >= 0; i-- {
        for j := len2 - 1; j >= 0; j-- {
            product := int(num1[i]-'0') * int(num2[j]-'0')
            temp := product + result[i+j+1]
            result[i+j+1] = temp % 10
            result[i+j] += temp / 10
        }
    }
    
    // Convert the result array to string
    var resultStr strings.Builder
    for i := range result {
        if !(resultStr.Len() == 0 && result[i] == 0) {
            resultStr.WriteString(string(result[i] + '0'))
        }
    }
    
    return resultStr.String()
}
