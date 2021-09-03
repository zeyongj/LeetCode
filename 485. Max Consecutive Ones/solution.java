class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0;
        int count = 0;
        int ans = 0;
        int size = nums.length;
        if (size == 0)
            return ans;
        else {
            for (int i = 0; i < size; i ++) {
            if (nums[i] == 1) {
                count ++;
            }
            else {
                result = Math.max(result, count);
                count = 0;
            }
        }
        }
        ans = Math.max(result, count);
        return ans;
    }
}
