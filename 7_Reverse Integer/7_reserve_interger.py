class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit = 2**31
        if x>=0:
            result = int(str(x)[::-1])
        else:
            result = -1*int(str(abs(x))[::-1])
        if abs(result) >limit:
            return 0
        else:
            return result