# Array # Breadth-First Search # Matrix
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        dirs = [(-1, 1), (0, 1), (1, 1), (1, 0),
                (-1, -1), (0, -1), (-1, 0), (0, 0)]
        while queue:
            x, y, dist = queue.popleft()
        # 목표지점인지 확인
        # 0인지 확인
        #
