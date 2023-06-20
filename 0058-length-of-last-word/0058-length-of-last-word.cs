int lengthOfLastWord(char * s){
    int length = strlen(s);
    int count = 0;
    int pos = length - 1;

    // Skip trailing spaces if any
    while (pos >= 0 && s[pos] == ' ') {
        --pos;
    }

    // Count characters in the last word
    while (pos >= 0 && s[pos] != ' ') {
        --pos;
        ++count;
    }

    return count;
}