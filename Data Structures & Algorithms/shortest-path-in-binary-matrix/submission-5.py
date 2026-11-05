from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # If start or end is blocked
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque()
        queue.append((0, 0, 1))  # row, col, path length

        # Mark start as visited
        grid[0][0] = 1

        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1),    # right
            (-1, -1),  # up-left
            (-1, 1),   # up-right
            (1, -1),   # down-left
            (1, 1)     # down-right
        ]

        while queue:
            row, col, distance = queue.popleft()

            # If we reached bottom-right
            if row == n - 1 and col == n - 1:
                return distance

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < n
                    and 0 <= new_col < n
                    and grid[new_row][new_col] == 0
                ):
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col, distance + 1))

        return -1