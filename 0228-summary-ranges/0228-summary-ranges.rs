impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut hm:std::collections::HashMap<i32,Vec<String>> = std::collections::HashMap::new();
        if nums.is_empty(){
            return vec![];
        }
        let mut last = nums[0];
        let mut x = 0;
        let mut ans = vec![];
        hm.insert(x, vec![nums[0].to_string()]);
        for n in nums.clone().into_iter().skip(1){
            if n -last == 1{
                hm.entry(x).or_insert(Vec::new()).push(n.to_string());
            }else{
                x += 1;
                hm.insert(x, vec![n.to_string()]);
            }
            last = n;
        }
        let mut hm_vec = hm.into_iter().collect::<Vec<_>>();
        hm_vec.sort_by(|a,b| a.0.cmp(&b.0));
        for (_,val) in hm_vec.into_iter(){
            if val.len() == 1{
                ans.push(val.join(""));
            }else{
                let temp = vec![val.first().unwrap().clone(),val.last().unwrap().clone()];
                ans.push(temp.join("->"));
            }
        }
        ans
    }
}