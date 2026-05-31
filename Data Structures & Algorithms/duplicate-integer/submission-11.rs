impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
  let mut map: HashMap<i32, i32> = HashMap::new();
    for x in nums {
        if map.contains_key(&x) {
            return true;
        } else {
            map.insert(x, 0);
        }
    }
    return false;

    }
}
