class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        length = len(s)
        reverse = s[::-1]
        integer = 0
        for i in range(0, length):
            if i != 0:
                if roman_list[reverse[i]] < roman_list[reverse[i - 1]]:
                    sign = -1
                else:
                    sign = 1
            else:
                sign = 1
            integer += sign * roman_list[reverse[i]]
        return integer