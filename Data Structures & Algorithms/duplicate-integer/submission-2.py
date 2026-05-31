class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for x in nums:
            if x in s: return True
            else:
                s[x] = 1
        return False