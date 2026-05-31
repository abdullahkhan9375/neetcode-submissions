impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
    let mut new_arr = Vec::with_capacity(nums.len() * 2);
    for i in 0..nums.len() * 2 {
        new_arr.push(nums[i % nums.len()])
    }
    new_arr
    }
}
