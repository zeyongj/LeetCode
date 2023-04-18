#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void generateParenthesisHelper(char **result, int *index, char *current, int open, int close, int n) {
    if (strlen(current) == n * 2) {
        result[*index] = malloc(sizeof(char) * (n * 2 + 1));
        strcpy(result[*index], current);
        (*index)++;
        return;
    }

    if (open < n) {
        char *newCurrent = malloc(sizeof(char) * (n * 2 + 1));
        memset(newCurrent, '\0', n * 2 + 1);
        strcpy(newCurrent, current);
        newCurrent[open + close] = '(';
        generateParenthesisHelper(result, index, newCurrent, open + 1, close, n);
        free(newCurrent);
    }
    
    if (close < open) {
        char *newCurrent = malloc(sizeof(char) * (n * 2 + 1));
        memset(newCurrent, '\0', n * 2 + 1);
        strcpy(newCurrent, current);
        newCurrent[open + close] = ')';
        generateParenthesisHelper(result, index, newCurrent, open, close + 1, n);
        free(newCurrent);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char **generateParenthesis(int n, int *returnSize) {
    int maxCombinations = 1;
    for (int i = n + 1; i <= 2 * n; i++) {
        maxCombinations *= i;
    }
    for (int i = 1; i <= n; i++) {
        maxCombinations /= i;
    }

    *returnSize = 0;
    char **result = malloc(sizeof(char *) * maxCombinations);
    char *current = malloc(sizeof(char) * (n * 2 + 1));
    memset(current, '\0', n * 2 + 1);

    generateParenthesisHelper(result, returnSize, current, 0, 0, n);

    free(current);
    return result;
}
