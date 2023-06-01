use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<String, Vec<String>> = HashMap::new();
        for s in strs {
            let mut chars: Vec<char> = s.chars().collect();
            chars.sort();
            let key = chars.into_iter().collect::<String>();
            map.entry(key).or_default().push(s);
        }
        map.into_iter().map(|(_, v)| v).collect()
    }
}
