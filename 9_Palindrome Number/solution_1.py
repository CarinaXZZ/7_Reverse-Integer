class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            length = 0
            y = x
            while (y != 0):
                y = y / 10
                length += 1
            palindrome = 0
            z = x
            for i in range(1, length + 1):
                if z % 10 == x / (10 ** (length - i)) % 10:
                    palindrome += 1
                z = z / 10
            if palindrome == length:
                return True
            else:
                return False
        else:
            return False