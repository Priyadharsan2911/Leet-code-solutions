class Solution:

  def hasValidPath(self, grid: list[list[str]]) -> bool:
    m, n = len(grid), len(grid[0])

    # A valid path length is m + n - 1, which must be even.
    # Also, path must start with '(' and end with ')'.
    if (m + n - 1) % 2 != 0 or grid[0][0] == ")" or grid[-1][-1] == "(":
      return False

    # memo[r][c][open_count] tracks if a path from (r, c) with open_count balance reaches target
    memo = {}

    def dfs(r: int, c: int, open_count: int) -> bool:
      if grid[r][c] == "(":
        open_count += 1
      else:
        open_count -= 1

      # If open_count drops below 0, it's an invalid parentheses prefix
      if open_count < 0:
        return False

      # Base case: reached bottom-right cell
      if r == m - 1 and c == n - 1:
        return open_count == 0

      # Return cached result if already visited with current state
      state = (r, c, open_count)
      if state in memo:
        return memo[state]

      # Explore moving down or right
      res = False
      if r + 1 < m:
        res = res or dfs(r + 1, c, open_count)
      if c + 1 < n and not res:
        res = res or dfs(r, c + 1, open_count)

      memo[state] = res
      return res

    return dfs(0, 0, 0)