class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if length matches and goal is a substring of s + s
        return len(s) == len(goal) and goal in (s + s)