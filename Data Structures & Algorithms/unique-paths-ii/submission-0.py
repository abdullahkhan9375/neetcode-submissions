class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        grid = obstacleGrid
        cache = {}
        def dfs(r, c, grid, cache):
            if r == ROWS or c == COLS:
                return 0
            
            if grid[r][c] == 1:
                return 0
            
            if (r,c) in cache and cache[(r,c)] > 0:
                return cache[(r,c)] 
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            cache[(r, c)] = dfs(r + 1, c, grid, cache) + dfs(r, c + 1, grid, cache)
            return cache[(r, c)]
        
        count = dfs(0, 0, grid, cache)
        return count

        