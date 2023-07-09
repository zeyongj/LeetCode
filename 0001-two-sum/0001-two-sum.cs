/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

struct intPair {
    int x;
    int order;
};

int compare(const void *a, const void *b) {
    struct intPair *p = (struct intPair *) a;
    struct intPair *q = (struct intPair *) b;
    return p->x - q->x;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i, j, *output;
    output = malloc(2 * sizeof(int));
    *returnSize = 2;
    struct intPair *arr = malloc(numsSize * sizeof(struct intPair));
    for (i = 0; i < numsSize; ++i) {
        arr[i].x = nums[i];
        arr[i].order = i;
    }
    qsort(arr, numsSize, sizeof(struct intPair), compare);
    i = 0;
    j = numsSize - 1;
    while (arr[i].x + arr[j].x != target) {
        while (arr[i].x + arr[j].x < target) {
            ++i;
        }
        while (arr[i].x + arr[j].x > target) {
            --j;
        }
    }
    output[0] = arr[i].order;
    output[1] = arr[j].order;
    free(arr);
    return output;
}