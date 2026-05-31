impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
    let mut map: HashSet<i32> = HashSet::new();
    for x in nums {
        if map.contains(&x) {
            return true;
        }
        map.insert(x);
    }
    false
    }
}
