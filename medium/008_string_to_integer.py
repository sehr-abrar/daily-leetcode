# 8. Medium: String to Integer

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # remove leading whitespace
        s = s.lstrip()

        if not s:
            return 0

        # check for optional sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # read digits and build the number
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1

        result *= sign

        # clamp the result within 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
