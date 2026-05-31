impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
  let mut map: HashSet<i32> = HashSet::new();
    for x in nums {
        if map.get(&x) != None {
            return true;
        }
        map.insert(x);
    }
    return false;
    }
}
