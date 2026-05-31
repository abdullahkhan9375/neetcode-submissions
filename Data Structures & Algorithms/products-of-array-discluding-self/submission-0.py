class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = []
        idx1 = 0
        mult = 1
        while idx1 < len(nums):
            for idx in range(len(nums)):
                if idx != idx1:
                    mult *= nums[idx]
            x.append(mult)
            mult = 1
            idx1 += 1

        return x 
