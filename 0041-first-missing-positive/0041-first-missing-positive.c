#include <stdlib.h>

void swap(int* nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

int firstMissingPositive(int* nums, int numsSize){
    for(int i = 0; i < numsSize; ++i) {
        while(nums[i] > 0 && nums[i] <= numsSize && nums[nums[i] - 1] != nums[i]) {
            swap(nums, i, nums[i] - 1);
        }
    }
    
    for(int i = 0; i < numsSize; ++i) {
        if(nums[i] != i + 1) {
            return i + 1;
        }
    }
    
    return numsSize + 1;
}
