# 7. Medium: Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # define 32-bit integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # get sign and absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)

        # reverse digits using string manipulation
        reversed_str = str(x)[::-1]
        reversed_int = int(reversed_str) * sign

        # check for overflow
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0

        return reversed_int
