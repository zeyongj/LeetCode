class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        
        // Find the index i such that nums[i] < nums[i+1]
        while (i >= 0 && nums[i] >= nums[i+1]) {
            i--;
        }
        
        // If such i is found, then find the index j such that nums[j] > nums[i] and j >= i
        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        
        // Reverse the elements from index i+1 to the end of the array
        reverse(nums, i+1);
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }
}
