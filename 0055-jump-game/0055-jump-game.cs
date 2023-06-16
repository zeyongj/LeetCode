public class Solution {
    public bool CanJump(int[] nums) {
        int len = nums.Length;
        int lastGoodIndex = len - 1;
        for (int i = len - 1; i >= 0; i--) {
            if (i + nums[i] >= lastGoodIndex) {
                lastGoodIndex = i;
            }
        }
        return lastGoodIndex == 0;                
    }
}