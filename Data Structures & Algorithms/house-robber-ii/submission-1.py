class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums1 = nums[1:]
        nums2 = nums[0:-1]

        memo1 = [-1] * len(nums)
        memo2 = [-1] * len(nums2)

        if len(nums) < 2:
            return nums[0]
        def dfs(i, n, memo):
            if i >= len(n):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dfs(i + 1, n, memo), n[i] + dfs(i + 2, n, memo))
            return memo[i]
        return max(dfs(0, nums1, memo1), dfs(0, nums2, memo2))
        