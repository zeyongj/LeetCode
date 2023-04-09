#include <stdlib.h>
#include <limits.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int abs_diff(int a, int b) {
    return a > b ? a - b : b - a;
}

int threeSumClosest(int* nums, int numsSize, int target){
    qsort(nums, numsSize, sizeof(int), compare);

    int closest_sum = nums[0] + nums[1] + nums[2];
    int min_diff = abs_diff(target, closest_sum);

    for (int i = 0; i < numsSize - 2; i++) {
        int left = i + 1;
        int right = numsSize - 1;

        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            int diff = abs_diff(target, sum);

            if (diff < min_diff) {
                min_diff = diff;
                closest_sum = sum;
            }

            if (sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            } else {
                return target; // The sum is equal to the target, so it's the closest.
            }
        }
    }

    return closest_sum;
}