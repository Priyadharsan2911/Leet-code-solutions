class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        # Step 1: Simulate gravity for each row in the original box
        for i in range(m):
            empty_pos = n - 1  # Track the rightmost available empty cell
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == "*":
                    empty_pos = j - 1  # Obstacle blocks stones, move pointer left
                elif boxGrid[i][j] == "#":
                    # Move stone to the rightmost empty position
                    boxGrid[i][j] = "."
                    boxGrid[i][empty_pos] = "#"
                    empty_pos -= 1
                else:
                    # Keep empty_pos as is if we encounter '.'
                    pass

        # Step 2: Rotate the box 90 degrees clockwise
        # An m x n matrix becomes an n x m matrix
        res = [[""] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = boxGrid[r][c]

        return res