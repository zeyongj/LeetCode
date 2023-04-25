int removeDuplicates(int* nums, int numsSize){
    if (numsSize == 0) {
            return 0;
        }

        int uniqueIndex = 0;
        for (int i = 1; i < numsSize; i++) {
            if (nums[i] != nums[uniqueIndex]) {
                uniqueIndex++;
                nums[uniqueIndex] = nums[i];
            }
        }

        return uniqueIndex + 1;
}