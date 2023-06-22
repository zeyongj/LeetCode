impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
	intervals.sort_unstable_by(|x, y| x[0].cmp(&y[0]));

	let mut res = Vec::new();

	let (mut start, mut end) = (intervals[0][0], intervals[0][1]);
	for interval in intervals.into_iter().skip(1) {
		let (curr_start, curr_end) = (interval[0], interval[1]);
		if curr_start > end {
			res.push(vec![start, end]);
			start = curr_start;
			end = curr_end;
		} else if curr_end > end {
			end = curr_end;
		}
	}

	res.push(vec![start, end]);

	res
}
}