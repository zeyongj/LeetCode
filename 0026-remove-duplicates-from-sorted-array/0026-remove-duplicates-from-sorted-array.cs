public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int size = nums.Length;
        if (size == 0) {
            return 0;
        }

        int uniqueIndex = 0;
        for (int i = 1; i < size; i++) {
            if (nums[i] != nums[uniqueIndex]) {
                uniqueIndex++;
                nums[uniqueIndex] = nums[i];
            }
        }

        return uniqueIndex + 1;
    }
}