# 10. Hard: Regular Expression Matching

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        # create a dp table with (m+1) x (n+1), initialized to false
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # empty string matches empty pattern
        dp[0][0] = True

        # handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # current characters match
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # zero occurrence of the previous character
                    dp[i][j] = dp[i][j - 2]
                    # one or more occurrence if previous character matches
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]
