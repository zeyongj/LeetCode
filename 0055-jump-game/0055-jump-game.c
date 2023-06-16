bool canJump(int* nums, int numsSize){
        int lastGoodIndex = numsSize - 1;
        for (int i = numsSize - 1; i >= 0; i--) {
            if (i + nums[i] >= lastGoodIndex) {
                lastGoodIndex = i;
            }
        }
        return lastGoodIndex == 0;
}