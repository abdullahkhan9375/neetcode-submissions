impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
    let x = nums.len() * 2;
    let mut new_arr = Vec::with_capacity(x);
    for i in 0..x {
        new_arr.push(nums[i % nums.len()])
    }
    new_arr
    }
}
