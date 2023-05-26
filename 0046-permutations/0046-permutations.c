/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void swap(int* nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

void backtrack(int* nums, int numsSize, int start, int** result, int* returnSize) {
    if (start == numsSize) {
        result[*returnSize] = (int*)malloc(numsSize * sizeof(int));
        memcpy(result[*returnSize], nums, numsSize * sizeof(int));
        (*returnSize)++;
    } else {
        for (int i = start; i < numsSize; i++) {
            swap(nums, start, i);
            backtrack(nums, numsSize, start + 1, result, returnSize);
            swap(nums, start, i); // backtrack
        }
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int maxReturnSize = 1;
    for (int i = 2; i <= numsSize; i++) {
        maxReturnSize *= i;
    }

    int** result = (int**)malloc(maxReturnSize * sizeof(int*));
    *returnSize = 0;
    *returnColumnSizes = (int*)malloc(maxReturnSize * sizeof(int));
    for (int i = 0; i < maxReturnSize; i++) {
        (*returnColumnSizes)[i] = numsSize;
    }

    backtrack(nums, numsSize, 0, result, returnSize);

    return result;
}
