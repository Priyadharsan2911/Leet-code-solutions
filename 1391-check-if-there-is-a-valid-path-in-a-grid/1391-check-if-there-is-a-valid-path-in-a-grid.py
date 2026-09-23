from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions connected by each street type: (row_change, col_change)
        streets = {
            1: [(0, -1), (0, 1)],   # Left, Right
            2: [(-1, 0), (1, 0)],   # Up, Down
            3: [(0, -1), (1, 0)],   # Left, Down
            4: [(0, 1), (1, 0)],    # Right, Down
            5: [(0, -1), (-1, 0)],  # Left, Up
            6: [(0, 1), (-1, 0)]    # Right, Up
        }
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                return True
            
            for dr, dc in streets[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if neighbor is unvisited
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Check if neighbor connects back in the opposite direction
                    if (-dr, -dc) in streets[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False