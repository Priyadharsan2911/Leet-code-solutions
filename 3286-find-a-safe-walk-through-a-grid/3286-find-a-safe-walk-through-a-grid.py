from collections import deque
from typing import List


class Solution:

  def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
    m, n = len(grid), len(grid[0])
    start_cost = grid[0][0]
    if start_cost >= health:
      return False

    dist = [[float("inf")] * n for _ in range(m)]
    dist[0][0] = start_cost
    dq = deque([(0, 0)])

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while dq:
      r, c = dq.popleft()
      cur_cost = dist[r][c]

      if r == m - 1 and c == n - 1:
        return cur_cost < health

      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < m and 0 <= nc < n:
          new_cost = cur_cost + grid[nr][nc]
          if new_cost < dist[nr][nc] and new_cost < health:
            dist[nr][nc] = new_cost
            if grid[nr][nc] == 0:
              dq.appendleft((nr, nc))
            else:
              dq.append((nr, nc))

    return dist[m - 1][n - 1] < health