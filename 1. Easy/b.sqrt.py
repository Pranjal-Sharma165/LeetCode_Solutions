class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        else:
            a = 1
            n = x
            while a <= n:
                mid = (a + n) // 2
                if mid * mid == x:
                    return mid
                elif mid * mid < x:
                    a = mid + 1
                else:
                    n = mid - 1
            return n