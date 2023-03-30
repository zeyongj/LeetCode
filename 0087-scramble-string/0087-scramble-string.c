#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return *(const char *)a - *(const char *)b;
}

unsigned long hash_key(const char *s1, const char *s2, int len) {
    return (unsigned long)s1 * 2971 + (unsigned long)s2 * 7933 + len;
}

bool is_scramble_recursive(const char *s1, const char *s2, int len, int memo[][31][31]) {
    if (len == 1) return *s1 == *s2;

    if (memo[s1 - s2 + 31 * 31][len][0] != 0) {
        return memo[s1 - s2 + 31 * 31][len][0] == 1;
    }

    char sorted_s1[len + 1], sorted_s2[len + 1];
    strncpy(sorted_s1, s1, len);
    strncpy(sorted_s2, s2, len);
    sorted_s1[len] = sorted_s2[len] = '\0';

    qsort(sorted_s1, len, sizeof(char), cmp);
    qsort(sorted_s2, len, sizeof(char), cmp);
    if (strcmp(sorted_s1, sorted_s2) != 0) return false;

    for (int i = 1; i < len; ++i) {
        if ((is_scramble_recursive(s1, s2, i, memo) && is_scramble_recursive(s1 + i, s2 + i, len - i, memo)) ||
            (is_scramble_recursive(s1, s2 + len - i, i, memo) && is_scramble_recursive(s1 + i, s2, len - i, memo))) {
            memo[s1 - s2 + 31 * 31][len][0] = 1;
            return true;
        }
    }

    memo[s1 - s2 + 31 * 31][len][0] = -1;
    return false;
}

bool isScramble(const char *s1, const char *s2) {
    int len = strlen(s1);
    if (len != strlen(s2)) return false;

    int memo[31 * 31][31][31];
    memset(memo, 0, sizeof(memo));

    return is_scramble_recursive(s1, s2, len, memo);
}
