class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        def dfs(r, c, seen, count):
            if r >= ROWS or c >= COLS:
                return 0
            if r < 0 or c < 0:
                return 0
            if not grid[r][c]:
                return 0
            if (r,c) in seen:
                return 0
            
            seen.add((r, c))
            return (1 + dfs(r + 1, c, seen, count) + dfs(r, c + 1, seen, count) + dfs(r - 1, c, seen, count) + dfs(r, c - 1, seen, count))
        
        for i in range(ROWS):
            for j in range(COLS):
                maxArea = max(maxArea, dfs(i, j, seen, count))
        
        return maxArea