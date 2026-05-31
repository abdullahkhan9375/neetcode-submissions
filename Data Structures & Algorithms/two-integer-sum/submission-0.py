class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(0, length):
            for j in range(i + 1, length):
                l1 = nums[i]
                l2 = nums[j]
                if (target - (l1 + l2)) == 0:
                    return [i, j]
                