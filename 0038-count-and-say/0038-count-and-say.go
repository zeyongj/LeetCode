import (
	"strconv"
	"strings"
)

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}

	previous := countAndSay(n - 1)
	var result strings.Builder
	count := 1

	for i := 1; i < len(previous); i++ {
		if previous[i] == previous[i-1] {
			count++
		} else {
			result.WriteString(strconv.Itoa(count))
			result.WriteByte(previous[i-1])
			count = 1
		}
	}

	result.WriteString(strconv.Itoa(count))
	result.WriteByte(previous[len(previous)-1])

	return result.String()
}
