impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        let mut result = Vec::new();
        Self::permute_helper(&mut nums, 0, &mut result);
        result
    }

    fn permute_helper(nums: &mut Vec<i32>, start: usize, result: &mut Vec<Vec<i32>>) {
        if start == nums.len() {
            result.push(nums.clone());
            return;
        }

        for i in start..nums.len() {
            nums.swap(start, i);
            Self::permute_helper(nums, start + 1, result);
            nums.swap(start, i); // backtrack
        }
    }
}
