# 9. Easy: Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # negative numbers are not palindromes
        if x < 0:
            return False

        # convert integer to string and compare with its reverse
        return str(x) == str(x)[::-1]
