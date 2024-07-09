class Solution {
    public int maximizeGreatness(int[] nums) {
        Arrays.sort(nums);
        int ans = 0;
        for (int num : nums) {
            if (nums[ans] < num) {
                ++ans;
            }
        }
        return ans;
    }
}