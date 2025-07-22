# 6. Medium: Zigzag Conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # edge case: if numRows is 1 or string is too short to zigzag
        if numRows == 1 or numRows >= len(s):
            return s

        # create an array of empty strings for each row
        rows = [''] * numRows
        index = 0  # current row
        step = 1   # direction: 1 for down, -1 for up

        # loop through each character in the string
        for char in s:
            # add the character to the current row
            rows[index] += char

            # reverse direction if we hit top or bottom
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            # move to the next row
            index += step

        # join all rows to get the final string
        return ''.join(rows)
