/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int getLen(char *s){
    int len = 0;
    while (s[len]) len++;
    return len;
}

char *centerJustify(char **words, int wordsSize, int *len, int startIndex, int endIndex, int maxWidth){
    int width = 0;
    for (int i=startIndex; i<=endIndex; i++) width += len[i];
    int totalSpace = maxWidth - width;
    int space = totalSpace / (endIndex - startIndex);
    int bonusSpace = totalSpace % (endIndex - startIndex);
    char *line = (char*)malloc(sizeof(char)*(maxWidth + 1));
    int index = 0;
    for (int i=startIndex; i<=endIndex; i++){
        // add space characters from the second word.
        if (i > startIndex){
            for (int j=0; j<space; j++) line[index++] = ' ';
            if (bonusSpace-- > 0) line[index++] = ' ';
        }
        // add the word to the line
        for (int j=0; j<len[i]; j++){
            line[index++] = words[i][j];
        }
    }
    line[index] = 0;
    
    return line;
}

char *leftJustify(char **words, int wordsSize, int *len, int startIndex, int endIndex, int maxWidth){
    char *line = (char*)malloc(sizeof(char)*(maxWidth + 1));
    int index = 0;
    for (int i=startIndex; i<=endIndex; i++){
        // add space characters from the second word.
        if (i > startIndex) line[index++] = ' ';
        // add the word to the line
        for (int j=0; j<len[i]; j++){
            line[index++] = words[i][j];
        }
    }
    for(int i = index; i<maxWidth; i++) line[index++] = ' ';
    line[index] = 0;
    
    return line;
}

char** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize) {
    if (wordsSize == 0){
		// return a line with all space charaters
		char **out = (char**)malloc(sizeof(char*));
		out[0] = (char*)malloc(sizeof(char) * maxWidth + 1);
		int index = 0;
		for (int i=0; i<maxWidth; i++) out[0][index++] = ' ';
		out[0][index] = 0;
		*returnSize = 1;
		return out;
	}
    int *len = (int*)calloc(wordsSize, sizeof(int));
    for (int i=0; i<wordsSize; i++){
        len[i] = getLen(words[i]);
    }
        
    int *startIndex = (int*)malloc(sizeof(int) * wordsSize);
    int startLen = 0;
    int width = 0, newWidth;
    startIndex[startLen++] = 0;
    for (int i=0; i<wordsSize; i++){
        newWidth = width + len[i];
        if (width > 0) newWidth++;
        
        if (newWidth > maxWidth){
        	startIndex[startLen++] = i;
        	width = len[i];
		}
        else width = newWidth;
    }
        
    char **out = (char**)malloc(sizeof(char*) * startLen);
    int index = 0;
    for (int i=0; i<startLen - 1; i++){
    	if (startIndex[i + 1] - startIndex[i] >= 2)
        	out[index++] = centerJustify(words, wordsSize, len, startIndex[i], startIndex[i + 1] - 1, maxWidth);
        else
        	out[index++] = leftJustify(words, wordsSize, len, startIndex[i], startIndex[i + 1] - 1, maxWidth);
    }
    out[index] = leftJustify(words, wordsSize, len, startIndex[startLen - 1], wordsSize - 1, maxWidth);
    
    free(startIndex);
    *returnSize = startLen;
    return out;
}