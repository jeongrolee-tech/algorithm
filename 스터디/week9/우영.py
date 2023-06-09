from collections import deque


def solution(grid):
    N = len(grid)
    if grid[0][0] or grid[N-1][N-1]:
        return -1
    if N == 1:
        return 1
    q = deque()
    q.append((0, 0, 1))
    dx = (0, 0, 1, -1, 1, 1, -1, -1)
    dy = (1, -1, 0, 0, -1, 1, 1, -1)

    while q:
        x, y, dist = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx == N-1 and ny == N-1:
                return dist + 1
            elif 0 <= nx < N and 0 <= ny < N and not grid[ny][nx]:
                q.append((nx, ny, dist+1))
                grid[ny][nx] = 1

    return -1
