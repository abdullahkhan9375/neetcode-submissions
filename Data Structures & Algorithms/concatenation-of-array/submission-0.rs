impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
    let mut new_arr = vec![0; nums.len() * 2];
    for i in 0..new_arr.len() {
        new_arr[i] = nums[i % nums.len()];
    }
    new_arr
    }
}
