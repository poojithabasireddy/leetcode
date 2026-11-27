
class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Step 1: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Convert digits
        num = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Step 4: Check overflow
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN

            num = num * 10 + digit
            i += 1

        return num * sign
