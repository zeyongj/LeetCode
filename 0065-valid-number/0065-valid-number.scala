func isNumber(s string) bool {
    state := 0
    finals := 0b101101000
    transfer := [][]int{
        {0, 1, 6, 2, -1},
        {-1, -1, 6, 2, -1},
        {-1, -1, 3, -1, -1},
        {8, -1, 3, -1, 4},
        {-1, 7, 5, -1, -1},
        {8, -1, 5, -1, -1},
        {8, -1, 6, 3, 4},
        {-1, -1, 5, -1, -1},
        {8, -1, -1, -1, -1},
    }

    for i := 0; i < len(s); i++ {
        id := make(s[i])
        if id < 0 {
            return false
        }
        state = transfer[state][id]
        if state < 0 {
            return false
        }
    }

    return (finals & (1 << state)) > 0
}

func make(c byte) int {
    switch c {
    case ' ':
        return 0
    case '+', '-':
        return 1
    case '.':
        return 3
    case 'e', 'E':
        return 4
    default:
        if c >= '0' && c <= '9' {
            return 2
        }
    }
    return -1
}
