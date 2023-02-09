impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 || num_rows as usize >= s.len() {
            return s
        }
        
        let mut res = String::new();
        let n = s.len();
        let cycle_len = 2 * num_rows as usize - 2;
        
        for i in 0..num_rows as usize {
            for j in (0..n).step_by(cycle_len) {
                if j + i < n {
                    res.push(s.chars().nth(j + i).unwrap());
                }
                if i != 0 && i != num_rows as usize - 1 && j + cycle_len - i < n {
                    res.push(s.chars().nth(j + cycle_len - i).unwrap());
                }
            }
        }
        
        res
    }
}
