impl Solution {
	pub fn length_of_last_word(s: String) -> i32 {
		let mut word = String::new();
		for ch in s.chars().rev() {
			if ch == ' '{
				if word.len() != 0 {
					break;
				}
			} else {
				word.push(ch)
			}
		}
		word.len() as _
	}
}