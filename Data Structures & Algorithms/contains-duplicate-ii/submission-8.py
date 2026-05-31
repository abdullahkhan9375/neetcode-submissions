class Solution:
    def check(self, nums, i, j, k):
        return nums[i] == nums[j] and abs(i - j) <= k

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
        return False