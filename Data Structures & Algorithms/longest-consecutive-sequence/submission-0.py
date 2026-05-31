class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        for i, x in enumerate(nums):
            m[x] = i
        
        start = None
        l = 0
        for x in nums:
            n = x - 1
            if n not in m:
                start = x
                b = True
                s = 0
                while b:
                    if start in m:
                        s += 1
                    else:
                        b = False
                    start = start + 1
                l = max(s, l)
        return l
