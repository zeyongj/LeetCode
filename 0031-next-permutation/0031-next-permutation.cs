using System;

public class Solution {
    public static void Swap(ref int a, ref int b) {
        int temp = a;
        a = b;
        b = temp;
    }

    public static void Reverse(int[] nums, int start, int end) {
        while (start < end) {
            Swap(ref nums[start], ref nums[end]);
            start++;
            end--;
        }
    }

    public void NextPermutation(int[] nums) {
        int i = nums.Length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.Length - 1;
            while (j > i && nums[j] <= nums[i]) {
                j--;
            }
            Swap(ref nums[i], ref nums[j]);
        }
        Reverse(nums, i + 1, nums.Length - 1);
    }
}