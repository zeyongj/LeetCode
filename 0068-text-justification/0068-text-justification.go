class Solution {
    func fullJustify(_ words: [String], _ maxWidth: Int) -> [String] {

        var lines: [String] = []

        var seenStrings: [String] = []
        var count = 0
        for w in words {

            let tmpCount = count + w.count + seenStrings.count

            if tmpCount > maxWidth {
                let totalSpaceCount = max(0, maxWidth - count)

                var currentIndex = 0
                for _ in 0..<totalSpaceCount {
                    seenStrings[currentIndex].append(" ")

                    if currentIndex + 1 < (seenStrings.count - 1) {
                        currentIndex += 1
                    } else {
                        currentIndex = 0
                    }
                }

                lines.append(seenStrings.joined())

                seenStrings = [w]
                count = w.count
            } else {
                seenStrings.append(w)
                count += w.count
            }
        }

        if seenStrings.count > 0 {
            let remainingSpaces = maxWidth - count - (seenStrings.count - 1)
            let spaces = String(repeating: " ", count: remainingSpaces)
            seenStrings.append(spaces)

            let line = String(seenStrings.joined(separator: " ").dropLast())
            lines.append(line)
        }

        return lines
    }
}