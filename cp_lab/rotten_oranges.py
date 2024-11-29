class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Queue for BFS, stores (row, col, minute)
        queue = []
        fresh_oranges = 0

        # Collect initial rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        # If there are no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0

        # Directions for 4-directional adjacency
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        minutes = 0

        while not len(queue) == 0:
            x, y, curr_min = queue.pop(0)
            minutes = curr_min

            for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if (nx >= 0) and (nx < m) and (ny >= 0) and (ny < n) and (grid[nx][ny] == 1):
                        grid[nx][ny] = 2 # Make it rotten
                        fresh_oranges -= 1
                        queue.append((nx, ny, curr_min + 1))

        return -1 if not fresh_oranges == 0 else minutes