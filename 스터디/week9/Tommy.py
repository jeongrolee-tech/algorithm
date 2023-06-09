class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        direction = [
            (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

        def neighbor_update(row, col):
            for diff_row, diff_col in direction:
                new_row = row + diff_row
                new_col = col + diff_col
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for new_row, new_col in neighbor_update(row, col):
                grid[new_row][new_col] = distance + 1
                queue.append((new_row, new_col))

        return -1
