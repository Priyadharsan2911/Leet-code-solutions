class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid_digits = {'3', '4', '7'}
        diff_digits = {'2', '5', '6', '9'}
        count = 0

        for i in range(1, n + 1):
            s = str(i)
            # A number is valid & changed if:
            # 1. Contains NO invalid digits (3, 4, 7)
            # 2. Contains AT LEAST ONE digit that changes upon rotation (2, 5, 6, 9)
            if not any(c in invalid_digits for c in s) and any(c in diff_digits for c in s):
                count += 1

        return count