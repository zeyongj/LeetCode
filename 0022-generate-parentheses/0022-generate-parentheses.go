func generateParenthesis(n int) []string {
	var result []string
	generateParenthesisHelper(&result, "", 0, 0, n)
	return result
}

func generateParenthesisHelper(result *[]string, current string, open int, close int, n int) {
	if len(current) == n*2 {
		*result = append(*result, current)
		return
	}

	if open < n {
		generateParenthesisHelper(result, current+"(", open+1, close, n)
	}

	if close < open {
		generateParenthesisHelper(result, current+")", open, close+1, n)
	}
}