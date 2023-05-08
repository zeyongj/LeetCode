/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

void dfs(int* candidates, int candidatesSize, int target, int start, int* stack, int top, int** res, int** columnSizes, int* returnSize) {
    if (target == 0) {
        res[*returnSize] = (int*) malloc(sizeof(int) * (top + 1));
        memcpy(res[*returnSize], stack, sizeof(int) * (top + 1));
        columnSizes[0][*returnSize] = top + 1;
        (*returnSize)++;
        return;
    }
    
    for (int i = start; i < candidatesSize; i++) {
        if (candidates[i] <= target) {
            stack[top + 1] = candidates[i];
            dfs(candidates, candidatesSize, target - candidates[i], i, stack, top + 1, res, columnSizes, returnSize);
        }
    }
}

int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes){
    int** res = (int**) malloc(sizeof(int*) * 150);
    int* stack = (int*) malloc(sizeof(int) * target);
    *returnSize = 0;
    *returnColumnSizes = (int*) malloc(sizeof(int) * 150);
    
    dfs(candidates, candidatesSize, target, 0, stack, -1, res, returnColumnSizes, returnSize);
    
    free(stack);
    
    return res;
}
