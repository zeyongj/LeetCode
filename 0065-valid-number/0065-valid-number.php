impl Solution {
    pub fn is_number(s: String) -> bool {
        if let Some(e) = s.chars().position(|c| c == 'e' || c == 'E') {
            Self::is_decimal(&s[0..e]) && Self::is_integer(&s[e + 1..])
        } else {
            Self::is_decimal(&s)
        }
    }
    fn is_decimal(s: &str) -> bool {
        let (mut num, mut dot) = (false, false);
        for (i, c) in s.chars().enumerate() {
            match c {
                '0'..='9' => num = true,
                '+' | '-' if i == 0 => {}
                '.' if !dot => dot = true,
                _ => return false,
            }
        }
        num
    }
    fn is_integer(s: &str) -> bool {
        let mut num = false;
        for (i, c) in s.chars().enumerate() {
            match c {
                '0'..='9' => num = true,
                '+' | '-' if i == 0 => {}
                _ => return false,
            }
        }
        num
    }
}