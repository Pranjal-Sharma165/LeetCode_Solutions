class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = 0
        x_orig = x
        if x >= 0:
            while x != 0:
                a = x % 10
                n = n * 10 + a
                x = x // 10

            if n == x_orig:
                return True
            else:
                return False

        else:
            return False
