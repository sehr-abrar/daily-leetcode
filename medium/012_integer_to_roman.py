# 12. Medium: Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # define roman numeral values and their symbols
        val_to_symbol = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        result = ''

        # loop through each value-symbol pair
        for value, symbol in val_to_symbol:
            # while the current value fits into num
            while num >= value:
                result += symbol
                num -= value

        return result
