class Solution:
    def isValid(self, s: str) -> bool:
        # If the string length is odd, it can't be balanced
        if len(s) % 2 != 0:
            return False

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Pop top element if stack is not empty, else assign a dummy character
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # Push opening brackets onto stack
                stack.append(char)

        # Valid if all opening brackets have been matched and popped
        return not stack