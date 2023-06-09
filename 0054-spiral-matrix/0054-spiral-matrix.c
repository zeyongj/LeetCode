#include <stdlib.h>

int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    *returnSize = matrixSize * *matrixColSize;
    int* res = (int*)malloc((*returnSize) * sizeof(int));

    int top = 0;
    int bottom = matrixSize - 1;
    int left = 0;
    int right = *matrixColSize - 1;
    int k = 0;
    
    while(true) {
        // Traverse from left to right.
        for (int i = left; i <= right; i++) res[k++] = matrix[top][i];
        if (++top > bottom) break;

        // Traverse from top to bottom.
        for (int i = top; i <= bottom; i++) res[k++] = matrix[i][right];
        if (--right < left) break;

        // Traverse from right to left.
        for (int i = right; i >= left; i--) res[k++] = matrix[bottom][i];
        if (--bottom < top) break;

        // Traverse from bottom to top.
        for (int i = bottom; i >= top; i--) res[k++] = matrix[i][left];
        if (++left > right) break;
    }
    
    return res;
}
