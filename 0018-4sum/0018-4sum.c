#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b) {
    return (*(int*)a) - (*(int*)b);
}

int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    if (numsSize < 4) {
        return NULL;
    }
    
    qsort(nums, numsSize, sizeof(int), compare);

    int** result = (int**)malloc(1000 * sizeof(int*));
    *returnColumnSizes = (int*)malloc(1000 * sizeof(int));
    
    for (int i = 0; i < numsSize - 3; ++i) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        
        for (int j = i + 1; j < numsSize - 2; ++j) {
            if (j > i + 1 && nums[j] == nums[j - 1]) {
                continue;
            }
            
            int left = j + 1;
            int right = numsSize - 1;
            
            while (left < right) {
                long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];
                
                if (sum == target) {
                    result[*returnSize] = (int*)malloc(4 * sizeof(int));
                    (*returnColumnSizes)[*returnSize] = 4;
                    result[*returnSize][0] = nums[i];
                    result[*returnSize][1] = nums[j];
                    result[*returnSize][2] = nums[left];
                    result[*returnSize][3] = nums[right];
                    ++(*returnSize);
                    
                    ++left;
                    --right;
                    
                    while (left < right && nums[left] == nums[left - 1]) {
                        ++left;
                    }
                    
                    while (left < right && nums[right] == nums[right + 1]) {
                        --right;
                    }
                } else if (sum < target) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
    }
    
    return result;
}
