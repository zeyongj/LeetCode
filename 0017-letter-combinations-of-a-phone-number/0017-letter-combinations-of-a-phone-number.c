#include <stdlib.h>
#include <string.h>

void backtrack(char *combination, char *digits, int index, char **phone, char ***result, int *returnSize) {
    if (index == strlen(digits)) {
        char *new_combination = (char *)malloc(strlen(combination) + 1);
        strcpy(new_combination, combination);
        result[0][*returnSize] = new_combination;
        (*returnSize)++;
        return;
    }

    char *letters = phone[digits[index] - '0'];
    for (int i = 0; i < strlen(letters); i++) {
        combination[index] = letters[i];
        combination[index + 1] = '\0';
        backtrack(combination, digits, index + 1, phone, result, returnSize);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char **letterCombinations(char *digits, int *returnSize) {
    if (digits == NULL || strlen(digits) == 0) {
        *returnSize = 0;
        return NULL;
    }

    char *phone[] = {
        "0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    int max_combinations = 1;
    for (int i = 0; i < strlen(digits); i++) {
        max_combinations *= strlen(phone[digits[i] - '0']);
    }

    char **result = (char **)malloc(max_combinations * sizeof(char *));
    char *combination = (char *)malloc((strlen(digits) + 1) * sizeof(char));

    *returnSize = 0;
    backtrack(combination, digits, 0, phone, &result, returnSize);

    free(combination);
    return result;
}
