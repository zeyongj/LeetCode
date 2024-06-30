impl Solution {
    pub fn longest_string(x: i32, y: i32, z: i32) -> i32 {
        let mut ans = 0;
        if x == y {
            ans = 2 * x.min(y);
        } else {
            ans = 2 * x.min(y) + 1;
        }

        ans += z;

        ans * 2
    }
}
