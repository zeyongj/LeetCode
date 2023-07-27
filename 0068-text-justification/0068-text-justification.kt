class Solution {
    private  val SEPARATOR = " " 
    
    fun fullJustify(words: Array<String>, maxWidth: Int): List<String> {

        val result = mutableListOf<String>() // keeps the lines as a sting in a paragraph
        val currentLineWords = mutableListOf<String>()// keeps track of all the words for the current line
        var availableSpacePerLine = maxWidth //  keeps track of the available space in the current line

        words.forEach { word ->
            availableSpacePerLine -= word.length
            when {
                (availableSpacePerLine == 0) -> { // the words perfectly fit
                    currentLineWords.add(word)
                    result.add(toLineString(availableSpacePerLine, currentLineWords))

                    // Start a new line
                    currentLineWords.clear()
                    availableSpacePerLine = maxWidth
                }
                (availableSpacePerLine < 0) -> { // too much words in a line adjust!
                    availableSpacePerLine += (word.length + 1) //remove the claimed space for current
                    result.add(toLineString(availableSpacePerLine, currentLineWords))

                    // Start a new line
                    currentLineWords.clear()
                    currentLineWords.add(word)
                    availableSpacePerLine = maxWidth - (word.length + 1)
                }
                (availableSpacePerLine > 0) -> { // space is still available in the current line
                    currentLineWords.add(word)
                    availableSpacePerLine--
                }
            }
        }

        // Process the last line if there is one
        if (currentLineWords.isNotEmpty()) {
            result.add(toLineString(availableSpacePerLine + 1, currentLineWords, true))
        }
        return result
    }
    

    private fun toLineString(
        noOfSpaceToBeDistributed: Int,
        wordsInLine: MutableList<String>,
        isLastLine: Boolean = false
    ): String {
        return if (wordsInLine.size == 1 || isLastLine) { // if there is only one word in a line or if the line is the last one , all the remaining spaces should just go to the end of the sentence
            wordsInLine.joinToString(SEPARATOR) + SEPARATOR.repeat(noOfSpaceToBeDistributed)
        } else { // other wise we have to evenly distribute the remaining lines
            val spaceToBeAddedToAllWords = (Math.floorDiv(
                noOfSpaceToBeDistributed,
                wordsInLine.lastIndex
            )) + 1 // the +1 is because we already take in to consideration a space when calculating noOfSpaceToBeDistributed
            
            for (i in 0 until noOfSpaceToBeDistributed % wordsInLine.lastIndex) {
                wordsInLine[i] += SEPARATOR
            }
            wordsInLine.joinToString(SEPARATOR.repeat(spaceToBeAddedToAllWords))
        }
    }
  
  
}