use std::collections::HashSet;

impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = vec![];
        let mut p: Vec<i32> = vec![];

        Self::_permute_unique(nums, &mut res, &mut p);
        res
    }

    fn _permute_unique(nums: Vec<i32>, res: &mut Vec<Vec<i32>>, p: &mut Vec<i32>) {
        if nums.is_empty() {
            res.push(p.to_vec());
            return;
        }

        let mut history: HashSet<i32> = HashSet::new();

        for (i, &value) in nums.iter().enumerate() {
            if history.get(&value).is_some() {
                continue;
            }

            history.insert(value);
            p.push(value);
            let mut tmp = nums.clone();
            tmp.remove(i);
            Self::_permute_unique(tmp, res, p);
            p.pop();
        }
    }
}
