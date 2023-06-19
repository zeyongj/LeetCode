impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut altitude = 0;
        let mut max_altitude = 0;
        
        for &g in &gain {
            altitude += g;
            max_altitude = std::cmp::max(max_altitude, altitude);
        }
        
        max_altitude
    }
}
