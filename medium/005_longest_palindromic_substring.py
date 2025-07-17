# 5. Medium: Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # edge case: if string is empty or has one character
        if len(s) < 2:
            return s

        start = 0
        max_len = 0

        # helper function to expand from the center
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return the length and new left index (after expanding one step too far)
            return left + 1, right - 1

        # loop through each character in the string
        for i in range(len(s)):
            # check for odd length palindrome
            l1, r1 = expand(i, i)
            # check for even length palindrome
            l2, r2 = expand(i, i + 1)

            # update longest palindrome if needed
            if r1 - l1 > max_len:
                start = l1
                max_len = r1 - l1

            if r2 - l2 > max_len:
                start = l2
                max_len = r2 - l2

        # return the longest palindromic substring
        return s[start:start + max_len + 1]
