# 13: Easy: Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # define symbol to value mapping
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        # loop through each character, except the last one
        for i in range(len(s) - 1):
            # if the current value is less than the next one, subtract it
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        # add the last character's value
        total += roman[s[-1]]

        return total
