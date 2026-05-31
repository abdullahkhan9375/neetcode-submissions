class Solution:
    def maxArea(self, heights: List[int]) -> int:
        idx1 = 0
        idx2 = len(heights) - 1
        vol = 0
        prev = 0
        while (idx1 < len(heights)):
            chos = 0
            if (heights[idx1] > heights[idx2]):
                chos = heights[idx2]
            else:
                chos = heights[idx1]
            vol = (idx2 - idx1) * chos
            if vol > prev:
                prev = vol
            idx2 -= 1
            if idx2 <= 0:
                idx1 += 1
                idx2 = len(heights) - 1
            if (idx1 > len(heights) -1 ):
                break
            if (idx2 < 0):
                break
        return prev
            
            
