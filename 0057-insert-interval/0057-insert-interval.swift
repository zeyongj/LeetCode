impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut answer: Vec<Vec<i32>> = Vec::with_capacity(intervals.len() + 1);
        let mut i = 0;
        while i < intervals.len() && intervals[i][1] < new_interval[0] {
            answer.push(intervals[i].clone());
            i += 1;
        }
        let mut new_interval = new_interval;
        while i < intervals.len() && intervals[i][0] <= new_interval[1] {
            new_interval[0] = std::cmp::min(new_interval[0], intervals[i][0]);
            new_interval[1] = std::cmp::max(new_interval[1], intervals[i][1]);
            i += 1;
        }
        answer.push(new_interval);
        while i < intervals.len() {
            answer.push(intervals[i].clone());
            i += 1;
        }
        answer
    }
}