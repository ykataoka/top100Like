import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

#        # Solution 1: Loop
#        # corner case:
#        if n == 0:
#            return False
#        if n == 1:
#            return True
#
#        # Loop
#        while n % 3 == 0:
#            n = n/3
#            print(n)
#            if n == 1:
#                return True
#        return False

        # Solution 2: Max of power of three
        # Key: Given the integer is 4 bytes as the max value, use the fixed number,
        # because 3 is the prime number
#        maxPowerThree = pow(3, 19)  # 3^19 < 2^31 < 3^20
#        return (n > 0) and (maxPowerThree % n == 0)

        # Solution 3: Use the Log10 (because Log makes some error)
        # n = 3^10, log10(3^10) = 10 log10(3), Thus if log10(n)/log10(3) -> integer, then should be power of three
        if n <= 0:
            return False
        logdivision = (math.log10(n) / math.log10(3))
        return (n > 0) and (logdivision % 1 == 0)
