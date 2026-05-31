impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
    let mut seen: HashSet<i32> = HashSet::new();
    for x in nums {
        if !seen.insert(x) {
            return true;
        }
    }
    false
    }
}
