/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

int** generateMatrix(int n, int* returnSize, int** returnColumnSizes) {
    int **matrix = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        matrix[i] = (int *)malloc(n * sizeof(int));
    }
    
    *returnSize = n;
    *returnColumnSizes = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        (*returnColumnSizes)[i] = n;
    }

    int top = 0, bottom = n - 1, left = 0, right = n - 1, num = 1;

    while (1) {
        for (int i = left; i <= right; i++) matrix[top][i] = num++;
        if (++top > bottom) break;

        for (int i = top; i <= bottom; i++) matrix[i][right] = num++;
        if (--right < left) break;

        for (int i = right; i >= left; i--) matrix[bottom][i] = num++;
        if (--bottom < top) break;

        for (int i = bottom; i >= top; i--) matrix[i][left] = num++;
        if (++left > right) break;
    }

    return matrix;
}
