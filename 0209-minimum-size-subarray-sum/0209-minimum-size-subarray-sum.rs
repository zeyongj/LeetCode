impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let hi = nums.iter().enumerate();
        let mut lo = hi.clone();
        let mut sum = 0;
        let mut min_len = None;
        for (hi_index, hi_num) in hi {
            sum += hi_num;
            while sum >= target {
                let (lo_index, lo_num) = lo.next().unwrap();
                min_len = Some(min_len.unwrap_or(usize::MAX).min(hi_index - lo_index + 1));
                sum -= lo_num;
            }
        }
        min_len.unwrap_or(0) as i32
    }
}