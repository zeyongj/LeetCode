import (
	"fmt"
)

func longestString(x int, y int, z int) int {
	ans := 0
	if x == y {
		ans = 2 * min(x, y)
	} else {
		ans = 2 * min(x, y) + 1
	}

	ans += z

	return ans * 2
}