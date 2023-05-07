#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char *countAndSayHelper(char *previous);

char *countAndSay(int n) {
    if (n == 1) {
        char *result = (char *)malloc(2 * sizeof(char));
        strcpy(result, "1");
        return result;
    }

    char *previous = countAndSay(n - 1);
    char *result = countAndSayHelper(previous);
    free(previous);
    return result;
}

char *countAndSayHelper(char *previous) {
    int length = strlen(previous);
    int result_capacity = length * 2 + 1;
    char *result = (char *)malloc(result_capacity * sizeof(char));
    int count = 1;
    int result_index = 0;

    for (int i = 1; i < length; ++i) {
        if (previous[i] == previous[i - 1]) {
            count++;
        } else {
            result_index += sprintf(result + result_index, "%d%c", count, previous[i - 1]);
            count = 1;
        }
    }

    result_index += sprintf(result + result_index, "%d%c", count, previous[length - 1]);
    result[result_index] = '\0';
    return result;
}
