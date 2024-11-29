class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        x, y = len(grid), len(grid[0])
        
        # Initialize DP table with the same size as grid
        dp = [[0 for _ in range(y)] for _ in range(x)]
        dp[0][0] = grid[0][0]  # Start point initialization

        # Fill the first row
        for j in range(1, y):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        # Fill the first column
        for i in range(1, x):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # Fill the rest of the DP table
        for i in range(1, x):
            for j in range(1, y):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        
        # The minimum path sum to reach the bottom-right cell
        return dp[x - 1][y - 1]