var sb strings.Builder

func fullJustify(words []string, maxWidth int) []string {
	var start, end, runeCount int
	var result = make([]string, 0, len(words))

	for start < len(words) {
		start = end
		runeCount = 0
		for end < len(words) && runeCount+end-start+len(words[end]) <= maxWidth {
			runeCount += len(words[end])
			end++
		}
		if start == end {
			break
		}
		if end == len(words) {
		// last line left justify
		str := strings.Join(words[start:end], " ")
			result = append(result, str+strings.Repeat(" ", maxWidth-len(str)))
		} else {
			result = append(result, generateString(words[start:end], runeCount, maxWidth))
		}
	}

	return result
}

func generateString(words []string, runeCount, maxWidth int) string {
	sb.Reset()
	var spaceCount, extraSpaces int
	if len(words) > 1 {
		spaceCount = (maxWidth - runeCount) / (len(words) - 1)
		extraSpaces = (maxWidth - runeCount) % (len(words) - 1)
	}

	for i := 0; i < len(words)-1; i++ {
		sb.WriteString(words[i])
		sb.WriteString(strings.Repeat(" ", spaceCount))
		if extraSpaces > 0 {
			sb.WriteString(" ")
			extraSpaces--
		}
	}

	sb.WriteString(words[len(words)-1])

	if sb.Len() < maxWidth {
		sb.WriteString(strings.Repeat(" ", maxWidth-sb.Len()))
	}

	return sb.String()[:maxWidth]
}