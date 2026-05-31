class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        s = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        s.add(tuple([nums[i], nums[j], nums[k]]))
        
        return [list(x) for x in s]
