from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        shortest_path = -1

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return shortest_path

        delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]
        q = deque([(0, 0, 1)])
        while q:
            i, j, cur_path = q.popleft()
            if i == n-1 and j == n-1:
                shortest_path = cur_path
                break
            for d1, d2 in delta:
                ni, nj = i+d1, j+d2
                if 0 <= ni < n and 0 <= nj < n and not grid[ni][nj]:
                    grid[ni][nj] = 1
                    q.append((ni, nj, cur_path + 1))
        return shortest_path
