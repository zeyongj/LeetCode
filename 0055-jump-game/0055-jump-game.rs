impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut last_good_index = nums.len() - 1;
        for i in (0..nums.len()).rev() {
            if i + nums[i] as usize >= last_good_index {
                last_good_index = i;
            }
        }
        last_good_index == 0
    }
}
